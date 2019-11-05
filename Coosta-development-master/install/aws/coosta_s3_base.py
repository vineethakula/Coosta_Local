"""
Simple wrapper around boto for S3 Operations
"""
import os

import boto
import boto.exception as boto_exception

BASE_COOSTA_BUCKET = 'coosta'   # Change for any other bucket
COOSTA_LOCATION = 'us-west-2'   # Change for any other region


class S3Base:
    def __init__(self):
        (self.aws_access_key_id,
         self.aws_secret_access_key) = self._load_id_and_secret_key_id()

    def upload_a_file(self, filepath, bucket):
        """
        Upload a file in S3

        :param filepath: full path of file to be uploaded
        :param bucket: bucket path
        :return: True if successful
        """
        filename = filepath.split('/')[-1]
        full_key_name = os.path.join(bucket, filename)

        try:
            bucket = self._connection().get_bucket(BASE_COOSTA_BUCKET)
            s3_key = bucket.new_key(full_key_name)
            s3_key.set_contents_from_filename(filepath)
            return True
        except boto_exception as exp:
            print exp
            return False

    def list_all_in_bucket(self, prefix=None):
        """
        List all files in a bucket

        :param prefix: prefix to narrow down to certain folders in a bucket.
        :return: Return a list of files/objects within the bucket.
        """
        bucket = self._connection().get_bucket(BASE_COOSTA_BUCKET)
        try:
            if prefix:
                return [item for item in bucket.list(prefix)]
            else:
                return [item for item in bucket.list()]
        except boto_exception.S3ResponseError as exp:
            print exp
            return False

    def delete_file_from_bucket(self, s3_file):
        """
        Delete key/object/file from S3 Bucket

        :param s3_file: file path on S3 object path
        :return: True if successful
        """
        bucket = self._connection().get_bucket(BASE_COOSTA_BUCKET)
        try:
            bucket.delete_key(s3_file)
            return True
        except boto_exception.S3ResponseError as exp:
            print exp
            return False

    def _connection(self):
        return boto.connect_s3(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )

    @staticmethod
    def _load_id_and_secret_key_id():
        """
        Try to read AWS access credentials from local config

        :return: credentials
        """
        credentials = {}
        try:
            # aws_file = os.path.join(os.environ['HOME'], '.aws', 'credentials')
            # with open(aws_file) as f:
            #     for line in f.readlines():
            #         if '=' in line:
            #             key, value = line.strip().split(' = ')
            #             credentials[key] = value
            # return (credentials['aws_access_key_id'],
            #         credentials['aws_secret_access_key'])
            return ('AKIAJURG2AWWJBV74QMQ',
                    'lH4NkK46hOGnY5YJud972Cdc2xaDFmpmzkjm7QWM')
        except IOError as exp:
            print exp
            print 'Credentials Empty'
