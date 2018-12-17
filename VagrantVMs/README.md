# VagrantVMs
This repository contains two already made Vagrant VMs that will run on virtualbox.

## Pre-requisites
- Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) for your Operating System.
- Download and install [Vagrant](https://www.vagrantup.com/downloads.html) for your Operationg System / distribution.

## Installation
- Clone the repository using `git clone`
- `cd VagrantVMs/vm1` (go to the project)
- `vagrant box add hashicorp/precise64`
- `cd VagrantVMs/vm2`
- `vagrant box add generic/fedora28`
- `vagrant up` to create the vitual machine.

###### To ssh into the virtual machine you can do:
`vagrant ssh`
use `CTRL + D` to disconnect from ssh.

## Removing the virtual machine

In case you don't want to use it anymore you can remove it using. `vagrant destory` while in project directory.



## create 2 fedora vms using vagrant - Fedora Project
### Task description

Virtual machines make administrative life so much easier. Not only can you test out new operating systems (without damaging your currently running OS), you can test new features, you can sandbox your web sites, you can develop new security models...the list goes on and on. But just as there are numerous reasons why you would want to run a virtual machine, there are numerous ways to create a virtual machine. Vagrant is an open-source software product for building and maintaining portable virtual software development environments. Vagrant is used to set up one or more virtual machines by:

- Importing pre-made images (called "boxes")
- Setting VM-specific settings (IP address, hostnames, port forwarding, memory, etc.)

### Goal

To create 2 VMs using vagrant.

### Suggested approach

- Install all of the components
- download appropriate iso
- Create a new virtual machine

### Deliverables

upload the vagrant file to the github repo and share it with the mentor (FAS: siddharthvipul1)