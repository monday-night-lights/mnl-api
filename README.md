# MNL Hockey League API

[![CircleCI](https://circleci.com/gh/monday-night-lights/mnl-api.svg?style=shield)](https://circleci.com/gh/monday-night-lights/mnl-api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6c339980c6f742c7a23de84e313e6af4)](https://www.codacy.com/app/monday-night-lights/mnl-api?utm_source=github.com&utm_medium=referral&utm_content=monday-night-lights/mnl-api&utm_campaign=badger)

A web API for managing Teams, Players, Games, and more for the Monday Night
Lights hockey league.

It is uses the [Django 2.0](https://docs.djangoproject.com/en/2.0/) web
framework, [Django Rest Framework 3.7](http://www.django-rest-framework.org/)
API library, and a [PostgreSQL 9.6](https://www.postgresql.org/docs/9.6/static/index.html)
database.

The Python code is written in accordance to the
[PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/#introduction).

## Development

To make set up as simple as possible across different operating systems, a
Vagrant file is set up to launch a Debian virtual machine using VirtualBox.
This VM can be treated like a production web server running locally on your
computer. [Docker Compose](https://docs.docker.com/compose/) is used to launch
the necessary services for running the application in a production-like manner.

In addition to the Django service, a separate [nginx](https://nginx.org/en/docs/)
service is used as a web proxy to connect the web application (running via
[Gunicorn](http://gunicorn.org/)) to web ports 80/443. It is also configured to
host static files separately from the web app.

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

    SECRET_KEY=dev_secret_key
    ALLOWED_HOSTS=localhost,127.0.0.1
    HOST=django
    DEBUG=True

    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432
    POSTGRES_DB=mnl_db
    POSTGRES_USER=mnl_db_user
    POSTGRES_PASSWORD=mnl_db_password

#### Run the Development Server

Use Vagrant to provision and run a Debian virtual development server

    $ vagrant plugin install vagrant-docker-compose vagrant-vbguest
    $ vagrant vbguest # https://stackoverflow.com/a/37706087/1797103
    $ vagrant up

The application will be running at [localhost:8888/](http://localhost:8888/).

### Running Django Management Commands

In order to run [Django commands](https://docs.djangoproject.com/en/2.0/ref/django-admin/),
SSH into the Vagrant VM and use `docker-compose exec` to execute commands
inside the Django container:

    $ vagrant ssh
    vagrant@contrib-jessie:~$ cd /src
    vagrant@contrib-jessie:/src$ docker-compose exec django <sh command>

For example, to run the
[Django shell](https://docs.djangoproject.com/en/2.0/ref/django-admin/#shell):

    vagrant@contrib-jessie:/src$ docker-compose exec django /venv/bin/python manage.py shell

#### Testing

Unit tests can be run with the built-in
[Django test runner](https://docs.djangoproject.com/en/2.0/topics/testing/overview/):

    vagrant@contrib-jessie:/src$ docker-compose exec django /venv/bin/python manage.py test
