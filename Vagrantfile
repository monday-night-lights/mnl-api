Vagrant.configure("2") do |config|
  config.vm.box = "debian/contrib-stretch64"
  config.vm.network "private_network", ip: "172.16.0.2"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = "2"
  end

  config.vm.provision "file", source: "./.bashrc", destination: "/home/vagrant/.bashrc"
  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.yml", rebuild: true, run: "always"
end
