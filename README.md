# MNL

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The Monday Night Lights Hockey League API built for managing Teams, Players, Seasons, Games, and more.

## Set up

This application can be run using Docker. If you cannot install Docker, a
Vagrantfile is provided for provisioning a Debian virtual machine as well.

First, clone this repository and copy the environment variables template to `.env`.

    $ git clone git@github.com/mnlhl:mnl.git
    $ cd mnl
    $ cp template.env .env  # variables are preset for dev but should be changed in production

### Running with Docker

1. Install [Docker](https://docs.docker.com/install/)
   and [Docker Compose](https://docs.docker.com/compose/install/)
1. Build and run the application containers using docker-compose:

        $ docker-compose up --build -d

1. View the running application in a browser at https://localhost

### Running with Vagrant

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and
   [Vagrant](https://www.vagrantup.com/downloads.html)
1. Add the [vagrant-docker-compose](https://github.com/leighmcculloch/vagrant-docker-compose)
   Vagrant plug-in and run the development VM:

        $ vagrant plugin install vagrant-docker-compose
        $ vagrant up

1. View the running application in a browser at https://172.16.0.2

### Running Tests

The unit tests can be run with `docker-compose exec django python manage.py test` (if you are using
Vagrant you will need to ssh into the VM first with `vagrant ssh`).

### Admin users

An admin user can be set up for development by running
`docker-compose exec django python manage.py createsuperuser`.

### SSL in development

**Note:** Since we are using a self-signed certificate for SSL in development,
your browser will warn that the page connection is insecure. Bypass the warning
by clicking "Advanced" and adding an exception for this certificate.

![Firefox Insecure Connection Warning](https://prod-cdn.sumo.mozilla.net/uploads/gallery/images/2018-07-24-17-48-12-79a9e2.png)

### Helpful Links

- [Docker](https://docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Vagrant](https://www.vagrantup.com/)
- [debian/contrib-stretch64](https://app.vagrantup.com/debian/boxes/contrib-stretch64)
  virtual box (`contrib-*` boxes include the `vboxfs` kernel module for shared folders)
- [Python 3.7](https://www.python.org/)
- [PEP 8 Python Style Guide](https://www.python.org/dev/peps/pep-0008/#introduction).
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [Django](https://djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [nginx](https://nginx.org/en/)
