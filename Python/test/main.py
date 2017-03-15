#!/usr/bin/python

import sys
import os
import socket
import Queue
import netaddr
import threading
import socketserver

def useage():
    print '''-h or --help   **---Help function
             -l or --alive  **---View the current live host
             -s or --scan   **---Scarch the network segment
    '''
live_host=Queue.Queue()
target_host=Queue.Queue()
server_listen_list_queue=Queue.Queue()
server_listen_list_th=Queue.Queue()

def socket_listen():
    global live_host
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',7777))
    server.listen(10000)

    while True:
        live_host.put(server.accept())


def main():
    global live_host
    global target_host
    global server_listen_list_queue
    global server_listen_list_th

    Current_path=os.getcwd()
    try:
        sys.path.append(Current_path+'/modules')
    except:
        print ''
        sys.exit(0)
    else:
        import ssh_cracked

    for i in range(5):
        server_listen_list_queue.put(threading.Thread(target=socket_listen))
    while not server_listen_list_queue.empty():
        server_listen_th=server_listen_list_queue.get()
        server_listen_th.start()
        server_listen_list_th.put(server_listen_th)


    while True:
        command=raw_input('Prism_Program:>>')
        if command == '-h' or command =='--help':
            useage()
            continue
        elif command == '--alive' or command =='-l':
            print str(live_host.qsize())+'Host computer'
        elif command == '--scan' or command=='-s':
            Net_list=netaddr.IPNetwork(command)
            for Net in Net_list:
                target_host.put(str(Net))
            threading.Thread()



if __name__ == '__main__':
    main()
