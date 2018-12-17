# ansible_autoinventoryfile
A playbook that creates a inventory file based on the given parameters. (This is for a Google Code-in Task)
- Make sure to edit `hosts` file with your node.
- Sample command to check if it works `ansible-playbook playbook.yml -e "host_addresses=192.168.0.123,192.168.0.134,192.84.2.3" -i hosts`. Go into the vm and check the created file :)

## Create dynamic inventory (Ansible) using Jinja2 templates - Fedora Project
### Task description

### Goal

To create an inventory file using ansible template feature

### Suggested approach

- pass variable in command using flag -e
- use jinja2 to define the structure to the inventory file
- use template module to pass variable to j2 files and create inventory

### Deliverables

- Share j2 file and the playbook in a repo/gist and mail the link to the mentor (FAS: siddharthvipul1)
