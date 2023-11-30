---
- name: Start Servers
  hosts: your_servers
  become: yes

  tasks:
    - name: Start the servers
      shell: "sudo systemctl start your_service_name"
