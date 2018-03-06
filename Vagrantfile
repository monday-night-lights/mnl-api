# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/contrib-jessie64"

  config.vm.network "private_network", ip: "172.30.0.10"

  config.vm.synced_folder ".", "/src", type: "virtualbox"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = "2"
  end

  config.vm.provision "shell", inline: <<-SHELL
    export DEBIAN_FRONTEND=noninteractive

    echo "# Running dist-upgrade"
    apt-get update 2>&1>/dev/null
    apt-get -y dist-upgrade 2>&1>/dev/null

    echo "# Installing Docker"
    apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common 2>&1>/dev/null
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" 2>&1>/dev/null
    apt-get update 2>&1>/dev/null
    apt-get -y install docker-ce 2>&1>/dev/null
    apt-get -y autoremove 2>&1>/dev/null

    echo "# Installing Docker Compose"
    curl -sL https://github.com/docker/compose/releases/download/1.14.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose

    echo "# Adding user 'vagrant' to docker group"
    usermod -aG docker vagrant 2>&1>/dev/null

    echo "# Building docker images"
    cd /src
    docker-compose build

    echo "# Starting application"
    docker-compose up -d
  SHELL
end
