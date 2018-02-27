#!/usr/bin/python

import nmap
import optparse
import os

exploit_list={'5666':cve_2013_1362}
def scan_nmap(subnet,target_port):
    target_ip_list=[]
    try:
        n_scan=nmap.PortScanner()
        print
        n_scan.scan(hosts=subnet,ports=target_port,arguments='--open -n')
        for target_ip in n_scan.all_hosts():
            target_ip_list.append(target_ip)
        if target_ip_list==[]:
            print 'No targets!!!'
        return target_ip_list
    except:
        print 'sorry you scan false!!!'


def cve_2013_1362(ConfigFile):


def exploit_write(ConfigFile,ports):
    for exploit in exploit_list:




def main():
    parser=optparse.OptionParser()
    parser.add_option('-n','--net',action='store',type='string',dest='nets')
    parser.add_option('-m','--mod',action='store',type='string',dest='mods')
    parser.add_option('-p','--port',action='store',type='string',dest='ports')
    (options,args)=parser.parse_args()
    subnets=options.nets
    mods=options.mods
    ports=options.ports
    ConfigFile = open('meta.rc', 'a')

    target_list=scan_nmap(subnets.ports)
    for ip in target_list:
        exploit_write(ip,ports)

    ConfigFile.close()

    os.system()


if __name__ == '__main__':
    main()


