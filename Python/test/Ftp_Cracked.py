#!/usr/bin/python

from ftplib import FTP
import netaddr
import sys
import os
import Queue
import threading

passwd=['123','root','ftp']
q=Queue.Queue(maxsize=1)
p=Queue.Queue(maxsize=1)
#th=len(sys.argv)-1
a=[]
username=['FTP','anonymous']
ftp_file=open('ftp_target_con.txt','a')
ftp_file_1=open('ftp_target_login.txt','a')
q.put(ftp_file)
p.put(ftp_file_1)

for i in range(len(sys.argv)):
    if i == 0:
        continue
    a.append(netaddr.IPNetwork(str(sys.argv[i])))

if a == []:
    os._exit(0)

def scan_ftp(ftp_net):
    global passwd
    global q
    global p
    global username


    for y in ftp_net:
        try:
            print 'connect to......'+str(y)
            ftp=FTP()
            #print str(y)
            ftp.connect(str(y),21,timeout=5)
            file_1=q.get()
            file_1.write(str(y)+'is connect!!!!\n')
            q.put(file_1)
        except:
            continue
        else:
            #try:
            try:
                print 'ftp login trying.....'
                ftp.login()
                file_2=p.get()
                print 'server:'+str(y)+' user:None passwd:None'
                file_2.write('server:'+str(y)+' user:None passwd:None\n')
                p.put(file_2)
                ftp.close()
                continue
            except:
                for u in username:
                    for pa in passwd:
                        try:
                            ftp.login(u,pa)
                        except:
                            continue
                        else:
                            file_2=p.get()
                            print 'server:'+str(y)+' user:'+str(u)+'passwd'+str(pa)
                            file_1.write(str(y)+' user:'+u+' passwd:'+pa+'\n')
                            p.put(file_2)
                            ftp.close()
            #except:
                #pass



def main():
    global a
    for x in a:
        threading.Thread(target=scan_ftp,args=(x,)).start()



if __name__ == '__main__':
    main()