# MNL Hockey League API

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6c339980c6f742c7a23de84e313e6af4)](https://www.codacy.com/app/jdrager2/mnl-api?utm_source=github.com&utm_medium=referral&utm_content=monday-night-lights/mnl-api&utm_campaign=badger)
[![CircleCI](https://circleci.com/gh/monday-night-lights/mnl-api/tree/master.svg?style=svg)](https://circleci.com/gh/monday-night-lights/mnl-api/tree/master)

A web API for managing Teams, Players, Games, and more for the Monday Night
Lights hockey league.

## Development

### Environment Setup

Install these tools to set up the development environment:

- [Vagrant](https://www.vagrantup.com/downloads.html)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

Clone the repository and navigate to the project directory.

    $ git clone git@github.com:monday-night-lights/mnl-api.git
    $ cd mnl-api

#### Set Environment Variables

The `dev.env` environment variables file is already created. These variables
should be changed for other environments (int.env, prod.env, etc.) but are fine
as they are for development purposes.

##### Default Dev Variables

    SECRET_KEY=your_secret_key
    ALLOWED_HOSTS=*
    HOST=http://localhost:8000
    DEBUG=True

    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432
    POSTGRES_DB=your_db
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password

#### Run the Development Server

Use Vagrant to provision and run a Debian virtual development server

    $ vagrant plugin install vagrant-docker-compose
    $ vagrant up

### Running Django Management Commands

In order to run [Django commands](https://docs.djangoproject.com/en/1.11/ref/django-admin/),
SSH into the Vagrant VM and use `docker-compose exec` to execute commands
inside the Django container:

    $ vagrant ssh
    vagrant@contrib-jessie:~$ cd /src
    vagrant@contrib-jessie:/src$ docker-compose exec django <sh command>

For example, to run the
[Django shell](https://docs.djangoproject.com/en/1.11/ref/django-admin/#shell):

    vagrant@contrib-jessie:/src$ docker-compose exec django /venv/bin/python manage.py shell

#### Testing

Unit tests can be run with the built-in
[Django test runner](https://docs.djangoproject.com/en/1.11/topics/testing/overview/):

    $ docker-compose exec django /venv/bin/python manage.py test
