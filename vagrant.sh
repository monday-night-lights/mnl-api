#!/bin/bash

export DEBIAN_FRONTEND=noninteractive
PROJECT_NAME='mnl'
DB_NAME=$PROJECT_NAME'_db'

sudo -E apt-get update
sudo -E apt-get install -y software-properties-common screen
sudo -E apt-get install -y dirmngr --install-recommends

# Install Python 3
if ! command -v python3.6; then
    sudo add-apt-repository 'deb http://ftp.de.debian.org/debian testing main'
    echo 'APT::Default-Release "stable";' | sudo tee -a /etc/apt/apt.conf.d/00local
    sudo -E apt-get update
    sudo -E apt-get -t testing install -y python3.6 python3-pip
    python3.6 -m pip install --user pipenv
fi

# Install PostgreSQL and create database
if ! command -v psql; then
    sudo -E apt-get install -y postgresql libpq-dev
    sudo su - postgres --command 'createuser -s vagrant'
    createdb $DB_NAME
fi

# Set up environment
cp /vagrant/.bashrc /home/vagrant/.bashrc
if [ ! -f /vagrant/.env ]; then
  cp /vagrant/template.env /vagrant/.env
fi
export PATH=$PATH:/home/vagrant/.local/bin

# Launch application
cd /vagrant
pipenv install
pipenv run python manage.py migrate
screen -dmS $PROJECT_NAME pipenv run python manage.py runserver 0.0.0.0:8000
