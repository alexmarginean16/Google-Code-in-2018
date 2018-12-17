#!/bin/bash

vagrant init generic/fedora29

echo 'Vagrant.configure("2") do |config|

  config.vm.box = "generic/fedora29"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end

end' > Vagrantfile

vagrant up

#vagrant provision

vagrant halt

vagrant destroy -f

rm Vagrantfile
rm -rf .vagrant
