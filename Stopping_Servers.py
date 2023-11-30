---
- name: Stop Servers
  hosts: your_servers
  become: yes

  tasks:
    - name: Stop the servers
      shell: "sudo systemctl stop your_service_name"
