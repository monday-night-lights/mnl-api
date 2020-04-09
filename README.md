# MNL

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The [Monday Night Lights Hockey League](http://mnlhl.com/) API built
for managing Teams, Players, Seasons, Games, and more.

## Set up

This application can be run using Docker. If you cannot install Docker, a
Vagrantfile is provided for provisioning a Debian virtual machine.

To get started, clone the repository. Then make a copy of `template.env` and rename it `.env`.

    $ git clone git@github.com/mnlhl:mnl.git
    $ cd mnl
    $ cp template.env .env  # variables are preset for dev but should be changed in production

### Running with Docker

1. Install [Docker](https://docs.docker.com/install/)
   and [Docker Compose](https://docs.docker.com/compose/install/)
1. Build and run the application containers using docker-compose:

        $ docker-compose up --build -d

1. View the running application in a browser at https://localhost

When you need to run a command inside a container, use:

    docker-compose exec container_name <command>

Or you can run a shell to enter the container and run commands inside

    docker-compose exec container_name /bin/sh
    # <command>

### Running with Vagrant

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and
   [Vagrant](https://www.vagrantup.com/downloads.html)
1. Add the [vagrant-docker-compose](https://github.com/leighmcculloch/vagrant-docker-compose)
   Vagrant plug-in and run the development VM:

        $ vagrant plugin install vagrant-docker-compose
        $ vagrant up

1. View the running application in a browser at https://172.16.0.2

### Running Tests

The unit tests can be run with:

    python manage.py test

### Admin users

An admin user can be added for development by running:

    python manage.py createsuperuser

### Python Requirements

We are using Pipenv to manage Python dependencies. This means there is a
`Pipfile` instead of the traditional `requirements.txt` file. To install
or update Python packages, run:

    pipenv install <package_name>
    pipenv update

    pipenv install --dev --system

This will update `Pipfile.lock` with the new version numbers, and then
install the packages globally within the `django` container.

### SSL in development

**Note:** Since we are using a self-signed certificate for SSL in development,
your browser will warn that the page connection is insecure. Bypass the warning
by clicking "Advanced" and adding an exception for this certificate.

![Firefox Insecure Connection Warning](https://prod-cdn.sumo.mozilla.net/uploads/gallery/images/2018-07-24-17-48-12-79a9e2.png)

### AWS S3 File Storage

To use AWS S3 for storing static files and user uploaded media, set the AWS
environment variables. The Django app will detect them and use the AWS storage
backends. If `AWS_STORAGE_BUCKET_NAME` is not set, Django's default storage
backends will be used. For more info, see
https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/.

### Helpful Links

#### Dev/Ops

- [Docker](https://docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Vagrant](https://www.vagrantup.com/)
- [debian/contrib-stretch64](https://app.vagrantup.com/debian/boxes/contrib-stretch64)
  virtual box (`contrib-*` boxes include the `vboxfs` kernel module for shared folders)
- [nginx](https://nginx.org/en/)

#### Database

- [PostgreSQL](https://www.postgresql.org/)

#### Python & Django

- [Python 3.7](https://www.python.org/)
- [PEP 8 Python Style Guide](https://www.python.org/dev/peps/pep-0008/#introduction)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [Django](https://djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
