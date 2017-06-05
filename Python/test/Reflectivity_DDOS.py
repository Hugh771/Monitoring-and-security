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
        scan_target_queue.put(str(ip))

scan_target_file_queue=Queue.Queue(maxsize=1)
server_target=open('server_target.txt','a')
scan_target_file_queue.put(server_target)

def Scan_target():
    global scan_target_queue
    global scan_target_file_queue

    while not scan_target_queue.empty():
        try:
            targe_ip=scan_target_queue.get()

            #dns_scan
            ans,uans=sr(IP(dst=targe_ip)/UDP()/DNS(qd=DNSQR(qname='yahoo.com.',qtype='ALL')),timeout=5)
            if ans.summary() ==None:
                print targe_ip+':53 port is down'
            elif len(ans[0])==2:
                if len(ans[0][1])>len(ans[0][0]):
                    f=scan_target_file_queue.get()
                    f.write(targe_ip+':53\n')
                    scan_target_file_queue.put(f)

            #snmp_scan
            asn,uans=sr(IP(dst=targe_ip)/UDP()/SNMP())
            if ans.summary()==None:
                print target_ip+':161 port is down'
            elif len(ans[0])==2:
                if len(ans[0][1])>len(ans[0][0]):
                    f=scan_target_file_queue.get()
                    f.write(targe_ip+':161\n')
                    scan_target_file_queue.put(f)

            #ntp_scan
            ans, uans = sr(IP()/UDP()/NTP())
            if ans.summary() == None:
                print targe_ip + ':53 port is down'
            elif len(ans[0]) == 2:
                if len(ans[0][1]) > len(ans[0][0]):
                    f = scan_target_file_queue.get()
                    f.write(targe_ip + ':53\n')
                    scan_target_file_queue.put(f)

        except:
            continue
        else:
            print targe_ip+'the scan ends'


def reflectivity_ddos():