#!/usr/bin/python

import nmap
from scapy.all import *
import threading
from optparse import OptionParser


def nmap_scan(targets):
    nmscan=nmap.PortScanner()
    nmscan.scan(hosts=targets,ports='53',arguments='-n --open')
    if nmscan.all_hosts() ==[]:
        return False

    host_list=[]
    for host in nmscan.all_hosts():
        ans,uans=sr(IP(dst=host)/UDP()/DNS(qd=DNSQR(qname='yahoo.com.',qtype='ALL')),timeout=3)
        try:
            if len(ans[0][1])>len(ans[0][0]):
                host_list.append(host)
        except:
            pass

    f=open('hosts.txt','a')
    for host in host_list:
        f.write(host+'\n')
    f.close()
    return host_list

def DNS_Reflectivity(hosts_list,target):
    for host in hosts_list:
        ans,uans=sr(IP(dst=host,src=target)/UDP()/DNS(qd=DNSQR(qname='yahoo.com.',qtype='ALL')),timeout=0.1)




def main():
    parser=OptionParser()
    parser.add_option('-t',action='store',type='string',dest='target_net_list')
    parser.add_option('-c',action='store',type='int',dest='thread_num')
    parser.add_option('-',action='store',type='int',dest='')
    (options,args)=parser.parse_args()

    target_list=options.target_net_list
    thread_num=options.thread_num

    hosts=nmap_scan(target_list)


def if __name__ == '__main__':
