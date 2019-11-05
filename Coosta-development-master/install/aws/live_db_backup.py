"""
Create Live database backup
Keep last(latest) 10 backups
"""
import os
import sys
import time

from coosta_s3_base import S3Base

# TODO: Removing hard coded values with argparse

DB_HOST = '54.213.231.130'   #LIVE DB
# DB_HOST = 'localhost'   #LIVE DB
DB_USER = 'coosta_db_user'
DB_USER_PASSWORD = 'coosta_db_pwd'
DB_NAME = 'coosta_db'
BACKUP_PATH = os.getcwd()
LAST_N_BACKUPS = 10

s3 = S3Base()


def db_backup(sql_file_name):
    """
    Create sql DB backup
    :param sql_file_name: full path of sql file in which backup need to be dump
    :return: True if successful
    """
    # Checking if backup folder already exists or not. If not, create it.
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)

    # Database backup process.
    dumpcmd = 'mysqldump -h{host} -p{pwd} -u{user} {dbname} > {filename}'.format(
        host=DB_HOST, pwd=DB_USER_PASSWORD, user=DB_USER, dbname=DB_NAME,
        filename=sql_file_name
    )
    print dumpcmd
    try:
        os.system(dumpcmd)
        return True
    except OSError as exp:
        print exp
        return False


def upload_on_s3(bucket, file):
    """
    upload file on S3
    :return: True if successful
    """
    return s3.upload_a_file(file, bucket)


def keep_only_last_n(n):
    """
    Keeps only last 10 db backups, remove others
    :return: True if successful
    """
    bucket_list = []

    server_result = s3.list_all_in_bucket(prefix='live-data/db-backup')
    # server_result = s3.list_all_in_bucket(prefix='dev-data/db-backup')
    if not server_result:
        return False
    for item in server_result:
        bucket_list.append([item.last_modified, item])

    # Sorted function below sort the list in ascending order of time
    keys_to_delete = sorted(bucket_list, cmp=lambda x, y: cmp(x[0], y[0]))

    # Removing first element as this is the parent folder itself,
    # deleting that will delete everything in that folder
    keys_to_delete = keys_to_delete[1:-1]

    # Removing the last(latest) LAST_N_BACKUPS files from the list
    keys_to_delete = keys_to_delete[:-n+1]

    for key in keys_to_delete:
        print 'Deleting {}'.format(key)
        server_result = s3.delete_file_from_bucket(key[-1])
        if not server_result:
            return False
    return True


if __name__ == '__main__':
    temp_filename = time.strftime('%m%d%Y-%H%M%S')
    filename = os.path.join(BACKUP_PATH, temp_filename + '.sql')
    bucket = os.path.join('live-data', 'db-backup')
    # bucket = os.path.join('dev-data', 'db-backup')

    if db_backup(filename):
        if upload_on_s3(bucket, filename):
            if keep_only_last_n(LAST_N_BACKUPS):
                print 'Success'
                sys.exit(0)
            else:
                print 'Failed: keep_only_last_n'
        else:
            print 'Failed: upload_on_s3'
    else:
        print 'Failed: db_backup'

    sys.exit(1)
