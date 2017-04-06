#!/usr/bin/python

import telnetlib

username_list=[]
passwd_list=[]

for passwd in file('./configuration/passwd.txt'):
    passwd_list.append(passwd)
for username in file('./configuration/username.txt'):
    username_list.append(username)

def scan(target_host,search_results):
    global passwd_list
    global username_list
    while not target_host.empty():
        target_info=target_host.get()
        if target_info[1] != 23:
            target_host.put(target_info)
            continue
        telnetlib.Telnet()




