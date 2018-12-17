# fedora-selinux-testcase
Automation of [testcase](https://fedoraproject.org/wiki/QA:Testcase_base_selinux) using ansible

Execute by running `./script.sh` (Make sure vagrant is installed on your machine)

[Recording of playbook running](https://asciinema.org/a/CYmKIiM5lUwzm9Fbr3M8VhiRD)

Latest [Recording](https://asciinema.org/a/yvWviJMKEXG3d0a5y7fSdcklO)

## Automate using ansible II - Fedora Project
### Task description

Automate https://fedoraproject.org/wiki/QA:Testcase_base_selinux using Ansible, bash and Python.

In the [link](https://fedoraproject.org/wiki/QA:Testcase_base_selinux), under how to test section, there are 2 points.

1. you have to download the iso, setup a vm/vagrant and complete testing. One simple step would be to download iso using wget module (example: get url from https://getfedora.org/en/atomic/download/) and then execute a shell script(use shell module and delegate_to: 127.0.0.1 to run it locally) to provision vm and to establish the connection.
2. Test getenforce output

submit asciinema recording and link to repo that has roles.