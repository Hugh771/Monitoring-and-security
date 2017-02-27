#!/usr/bin/python

from time import *
import psutil
import logging

Host_result={'cpu_info':{},'memory_info':{},'io_info':{},'net_info':{}}
Process_result={}

def Process_info(pid):

    ps={}
    p=psutil.Process(pid)
    ps['process']=p.name()
    ps['process_threads_num']=len(p.threads())
    ps['process_status']=p.status()
    ps['process_username']=p.username()
    ps['process_openfile']=[i.path for i in p.open_files()]
    ps['process_create_time']=p.create_time()
    ps['process_children']=[i.pid for i in p.children()]

    ps['process_cputimes']={}
    cpu_times=[i for i in p.cpu_times() ]
    ps['process_cputimes']['user']=cpu_times[0]
    ps['process_cputimes']['system']=cpu_times[1]
    ps['process_cputimes']['children_user']=cpu_times[2]
    ps['process_cputimes']['children_system']=cpu_times[3]

    uids=[i for i in p.uids()]
    ps['process_uids']={}
    ps['process_uids']['real']=uids[0]
    ps['process_uids']['effective']=uids[1]
    ps['process_uids']['saved']=uids[2]

    ps['process_gids']={}
    gids=[i for i in p.gids()]
    ps['process_gids']['real']=gids[0]
    ps['process_gids']['effective']=gids[1]
    ps['process_gids']['saved']=gids[2]

    ps['process_exe']=p.exe()
    ps['process_cwd']=p.cwd()
    ps['process_ppid']=p.ppid()

    #process_memory
    memory_info=[i for i in p.memory_info()]
    ps['process_memoryinfo']={}
    ps['process_memoryinfo']['rss']=memory_info[0]
    ps['process_memoryinfo']['vms']=memory_info[1]
    ps['process_memoryinfo']['shared']=memory_info[2]
    ps['process_memoryinfo']['text']=memory_info[3]
    ps['process_memoryinfo']['lib']=memory_info[4]
    ps['process_memoryinfo']['data']=memory_info[5]
    ps['process_memoryinfo']['dirty']=memory_info[6]

    memory_maps=[i.path for i in p.memory_maps()]
    ps['process_memorymaps']=memory_maps

    #process_io
    io_counters=[i for i in p.io_counters()]
    ps['process_io_counters']={}
    ps['process_io_counters']['read_count']=io_counters[0]
    ps['process_io_counters']['write_count']=io_counters[1]
    ps['process_io_counters']['read_bytes']=io_counters[2]
    ps['process_io_counters']['write_bytes']=io_counters[3]

    #process_net
    process_net=[i.laddr for i in p.connections()]
    ps['process_net']=process_net

    return ps


def Process_monitor_add():
    pids_add_initialization=[]
    for i in psutil.pids()
        pids_add_initialization.append(i)

    while True:
        for pid_now in psutil.pids():
            if pid_now in pids_add_initialization:
                continue
            elif pid_now not in pids_add_initialization:
                print pid_now
                pids_add_initialization.append(pid_now)
                try:
                    Process_result[str(pid_now)]=Process_info(pid_now)
                except:
                    continue
                else:
                    #Process_Data_Send()
                    pass


def Process_monitor_remove():
    pids_remove_initialization=[]

    for y in psutil.pids():
        pids_remove_initialization.append(y)

    while True:
        sleep(1800)
        pids_now=psutil.pids()
        for pid_initialization in pid_r_initialization:
            if pid_initialization in pids_now:
                continue
            elif pid_initialization not in pids_now:
                Process_Death_reminder(pid_initialization)
                pids_r_initialization.remove(pid_initialization)


def Process_Data_Send()
    global Process_result

#def Process_Death_reminder(pid_initialization):



def Host_info():
    global Host_result

    #cpu_info
    Host_result['cpu_info']['cpu_count']=psutil.cpu_count()

    cpu_time=[i for i in psutil.cpu_times()]
    Host_result['cpu_info']['cpu_times']={}
    Host_result['cpu_info']['cpu_times']['user']=cpu_time[0]
    Host_result['cpu_info']['cpu_times']['nice']=cpu_time[1]
    Host_result['cpu_info']['cpu_times']['system']=cpu_time[2]
    Host_result['cpu_info']['cpu_times']['idle']=cpu_time[3]
    Host_result['cpu_info']['cpu_times']['iowait']=cpu_time[4]
    Host_result['cpu_info']['cpu_times']['irq']=cpu_time[5]
    Host_result['cpu_info']['cpu_times']['softirq']=cpu_time[6]
    Host_result['cpu_info']['cpu_times']['steal']=cpu_time[7]
    Host_result['cpu_info']['cpu_times']['guest']=cpu_time[8]
    Host_result['cpu_info']['cpu_times']['guest_nice']=cpu_time[9]

    Host_result['cpu_info']['cpu_percent']=psutil.cpu_percent()


    # memory_info
    virtual_memory=[i for i in psutil.virtual_memory()]
    Host_result['memory_info']['virtual_memory']={}
    Host_result['memory_info']['virtual_memory']['total']=virtual_memory[0]
    Host_result['memory_info']['virtual_memory']['available']=virtual_memory[1]
    Host_result['memory_info']['virtual_memory']['percent']=virtual_memory[2]
    Host_result['memory_info']['virtual_memory']['used']=virtual_memory[3]
    Host_result['memory_info']['virtual_memory']['free']=virtual_memory[4]
    Host_result['memory_info']['virtual_memory']['active']=virtual_memory[5]
    Host_result['memory_info']['virtual_memory']['inactive']=virtual_memory[6]
    Host_result['memory_info']['virtual_memory']['buffers']=virtual_memory[7]
    Host_result['memory_info']['virtual_memory']['cached']=virtual_memory[8]
    Host_result['memory_info']['virtual_memory']['shared']=virtual_memory[9]

    swap_memory=[i for i in psutil.swap_memory()]
    Host_result['memory_info']['swap_memory']={}
    Host_result['memory_info']['swap_memory']['total']=swap_memory[0]
    Host_result['memory_info']['swap_memory']['used']=swap_memory[1]
    Host_result['memory_info']['swap_memory']['free']=swap_memory[2]
    Host_result['memory_info']['swap_memory']['percent']=swap_memory[3]
    Host_result['memory_info']['swap_memory']['sin']=swap_memory[4]
    Host_result['memory_info']['swap_memory']['sout']=swap_memory[5]


    #disk_info
    Host_result['io_info']['disk_partitions']={}
    for disk_partitions in psutil.disk_partitions():
        Host_result['io_info']['disk_partitions'][disk_partitions.mountpoint]={}
        Host_result['io_info']['disk_partitions'][disk_partitions.mountpoint]['device']=disk_partitions.device
        Host_result['io_info']['disk_partitions'][disk_partitions.mountpoint]['fstype']=disk_partitions.fstype
        Host_result['io_info']['disk_partitions'][disk_partitions.mountpoint]['fstype']=disk_partitions.fstype
        Host_result['io_info']['disk_partitions'][disk_partitions.mountpoint]['opts']=disk_partitions.opts

    Host_result['io_info']['disk_usage']={}
    for disk_mountpoint in Host_result['io_info']['disk_partitions']:
        disk_usage=psutil.disk_usage(disk_mountpoint)
        Host_result['io_info']['disk_usage'][disk_mountpoint]={}
        Host_result['io_info']['disk_usage'][disk_mountpoint]['total']=disk_usage.total
        Host_result['io_info']['disk_usage'][disk_mountpoint]['used']=disk_usage.used
        Host_result['io_info']['disk_usage'][disk_mountpoint]['free']=disk_usage.free
        Host_result['io_info']['disk_usage'][disk_mountpoint]['percent']=disk_usage.percent

    Host_result['io_info']['disk_io_counters']={}
    disk_io_counters=psutil.disk_io_counters(perdisk=True)
    for disk_io_counter in disk_io_counters:
        Host_result['io_info']['disk_io_counters'][disk_io_counter]={}
        Host_result['io_info']['disk_io_counters'][disk_io_counter]['read_count']=disk_io_counters[disk_io_counter].read_count
        Host_result['io_info']['disk_io_counters'][disk_io_counter]['write_count']=disk_io_counters[disk_io_counter].write_count
        Host_result['io_info']['disk_io_counters'][disk_io_counter]['read_bytes']=disk_io_counters[disk_io_counter].read_bytes
        Host_result['io_info']['disk_io_counters'][disk_io_counter]['write_bytes']=disk_io_counters[disk_io_counter].write_bytes
        Host_result['io_info']['disk_io_counters'][disk_io_counter]['read_time']=disk_io_counters[disk_io_counter].read_time
        Host_result['io_info']['disk_io_counters'][disk_io_counter]['write_time']=disk_io_counters[disk_io_counter].write_time
        Host_result['io_info']['disk_io_counters'][disk_io_counter]['read_merged_count']=disk_io_counters[disk_io_counter].read_merged_count
        Host_result['io_info']['disk_io_counters'][disk_io_counter]['write_merged_count']=disk_io_counters[disk_io_counter].write_merged_count
        Host_result['io_info']['disk_io_counters'][disk_io_counter]['busy_time']=disk_io_counters[disk_io_counter].busy_time


    #net_info
    Host_result['net_info']['net_io_counters']={}
    net_io_counters=psutil.net_io_counters(pernic=True)
    for net_io_counter in net_io_counters:
        Host_result['net_info']['net_io_counters'][net_io_counter]={}
        Host_result['net_info']['net_io_counters'][net_io_counter]['bytes_sent']=net_io_counters[net_io_counter].bytes_sent
        Host_result['net_info']['net_io_counters'][net_io_counter]['bytes_recv']=net_io_counters[net_io_counter].bytes_recv
        Host_result['net_info']['net_io_counters'][net_io_counter]['packets_sent']=net_io_counters[net_io_counter].packets_sent
        Host_result['net_info']['net_io_counters'][net_io_counter]['packets_recv']=net_io_counters[net_io_counter].packets_recv
        Host_result['net_info']['net_io_counters'][net_io_counter]['errin']=net_io_counters[net_io_counter].errin
        Host_result['net_info']['net_io_counters'][net_io_counter]['errout']=net_io_counters[net_io_counter].errout
        Host_result['net_info']['net_io_counters'][net_io_counter]['dropin']=net_io_counters[net_io_counter].dropin
        Host_result['net_info']['net_io_counters'][net_io_counter]['dropout']=net_io_counters[net_io_counter].dropout

    Host_result['net_info']['net_connections']={}
    net_connections=psutil.net_connections()
    for net_connection in net_connections:
        Host_result['net_info']['net_connections'][net_connection.pid]={}
        Host_result['net_info']['net_connections'][net_connection.pid]['status']=net_connection.status
        Host_result['net_info']['net_connections'][net_connection.pid]['laddr']=net_connection.laddr
        Host_result['net_info']['net_connections'][net_connection.pid]['raddr']=net_connection.raddr

    Host_result['net_info']['net_if_addrs']={}
    net_if_addrs=psutil.net_if_addrs()
    for net_if_addr in net_if_addrs:
        Host_result['net_info']['net_if_addrs'][net_if_addr]={}
        Host_result['net_info']['net_if_addrs'][net_if_addr]['address']=net_if_addrs[net_if_addr][0].address
        Host_result['net_info']['net_if_addrs'][net_if_addr]['netmask']=net_if_addrs[net_if_addr][0].netmask


if __name__ == '__main__':
    Process_monitor_add()