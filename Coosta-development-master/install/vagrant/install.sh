#!/usr/bin/env bash

echo 'install.sh is run !'
# Configuration
PROJECT_NAME=$1
MYSQL_PASSWORD=$2
PYTHON_VERSION=$3
VIRTUALENV_NAME=$PROJECT_NAME
HOME_DIR='/home/vagrant/'
PROJECTS_DIR="/vagrant/coosta/"
ROOT_DIR="/vagrant/"
echo "CONFIGURATION: PROJECT_NAME=$PROJECT_NAME, MYSQL_PASSWORD=$MYSQL_PASSWORD,\
  PYTHON_VERSION=$PYTHON_VERSION,\
  VIRTUALENV_NAME=$VIRTUALENV_NAME, HOME_DIR=$HOME_DIR"

# Essentials tasks
rm -f $HOME_DIR/postinstall.sh # remove useless stuff
echo "$HOME_DIR/postinstall.sh was removed"

echo 'APT deposit will be updated'
apt-get -y update
echo 'Done.'

echo 'Some essential packages will be installed'
apt-get -y install bc git-core build-essential
echo 'Done.'

# MySQL & create database
echo 'MySQL will be installed and configured'
debconf-set-selections <<< "mysql-server-5.5 mysql-server/root_password password $MYSQL_PASSWORD"
debconf-set-selections <<< "mysql-server-5.5 mysql-server/root_password_again password $MYSQL_PASSWORD"
apt-get -y install mysql-server
apt-get -y install mysql-client
apt-get -y install libmysqlclient-dev
echo "CREATE DATABASE IF NOT EXISTS $PROJECT_NAME CHARACTER SET utf8;" | mysql --host=localhost --user=root --password=$MYSQL_PASSWORD
echo 'Done.'

# Python + virtualenv
echo "A Python$PYTHON_VERSION will be initialized with a virtualenv"
apt-get -y install python python$PYTHON_VERSION python$PYTHON_VERSION-dev python-pip

pip install virtualenv
pip install virtualenvwrapper

echo '' >> $HOME_DIR.bashrc
echo '# CUSTOM' >> $HOME_DIR.bashrc
echo "export WORKON_HOME=$PROJECTS_DIR/virtualenvs" >> $HOME_DIR.bashrc
echo 'mkdir -p $WORKON_HOME' >> $HOME_DIR.bashrc
echo "export PROJECT_HOME=$PROJECTS_DIR/$PROJECT_NAME" >> $HOME_DIR.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> $HOME_DIR.bashrc
echo "workon $VIRTUALENV_NAME" >> $HOME_DIR.bashrc
echo "echo 'virtualenv acivated'" >> $HOME_DIR.bashrc
echo 'cd $PROJECT_HOME' >> $HOME_DIR.bashrc

export WORKON_HOME=$PROJECTS_DIR/virtualenvs
mkdir -p $WORKON_HOME
export PROJECT_HOME="$PROJECTS_DIR/$PROJECT_NAME"
source /usr/local/bin/virtualenvwrapper.sh

echo 'done.'

echo 'Virtualenv activation ...'
mkvirtualenv --python=/usr/bin/python$PYTHON_VERSION $VIRTUALENV_NAME
echo 'Virtualenv activating now'
su - vagrant -c "source /vagrant/coosta/virtualenvs/coosta/bin/activate"
echo "requirements installation ..."
pip install -r /home/vagrant/coosta/requirements.txt
echo "requirements updating ..."


# Set execute permissions on manage.py, as they get lost if we build from a zip file
chmod a+x /home/vagrant/coosta/coosta/manage.py
# Django project setup
su - vagrant -c "source /vagrant/coosta/virtualenvs/coosta/bin/activate && cd /home/vagrant/coosta/coosta && ./manage.py migrate && ./manage.py runserver"