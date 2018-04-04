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

  config.vm.provision "shell", path: "vagrant-provision.sh"
end
