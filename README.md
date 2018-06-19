# MNL Hockey League API

[![CircleCI](https://circleci.com/gh/monday-night-lights/mnl-api.svg?style=shield)](https://circleci.com/gh/monday-night-lights/mnl-api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6c339980c6f742c7a23de84e313e6af4)](https://www.codacy.com/app/monday-night-lights/mnl-api?utm_source=github.com&utm_medium=referral&utm_content=monday-night-lights/mnl-api&utm_campaign=badger)
![license](https://img.shields.io/github/license/monday-night-lights/mnl-api.svg?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/monday-night-lights/mnl-api.svg?style=flat-square)
![FTNS](https://img.shields.io/badge/Fuck%20The-North%20Stars-009639.svg?longCache=true&style=flat-square)

A web API for managing Teams, Players, Games, and more for the Monday Night
Lights hockey league.

It is uses the [Django 2.0](https://docs.djangoproject.com/en/2.0/) web
framework, [Django Rest Framework 3.7](http://www.django-rest-framework.org/)
API library, and a [PostgreSQL 9.6](https://www.postgresql.org/docs/9.6/static/index.html)
database.

The Python code is written in accordance to the
[PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/#introduction).

## Set up
1. Install [Vagrant](https://www.vagrantup.com/downloads.html)
1. Clone this repository and launch the development VM:

        $ git clone git@github.com:monday-night-lights/mnl-api.git
        $ cd mnl-api
        $ vagrant up

1. View the running application in a browser at http://172.30.0.10:8000/

## Development

- Use `vagrant ssh` to access the VM shell
- [Pipenv](https://pypi.org/project/pipenv/) is already installed on the VM and
  ready to use. You do not need to install or use virtualenv/virtualenvwrapper
- Use `pipenv run` to run a given command from the virtualenv, with any
  arguments forwarded
- Use `pipenv install [OPTIONS] [PACKAGE_NAME]` to install additional packages
  in the virtualenv

### Environment variables

A `.env` file is created when you first call `vagrant up` and should be
edited to match your project specifications. Be sure to change the `SECRET_KEY`
value for any production-like environments.

### Server Logs

The Django development server is running in a separate terminal session through
[GNU Screen](https://www.linode.com/docs/networking/ssh/using-gnu-screen-to-manage-persistent-terminal-sessions/).

- To view the Django server logs, run `screen -r`
- To exit the logs without killing the server, press **Ctrl + A + D**
- To restart the server if you kill it, run
  `screen -dmS <project_name> pipenv run python manage.py runserver 0.0.0.0:8000`

### Testing

Unit tests can be run with the
[Django test runner](https://docs.djangoproject.com/en/2.0/topics/testing/overview/):

    $ pipenv run python manage.py test
