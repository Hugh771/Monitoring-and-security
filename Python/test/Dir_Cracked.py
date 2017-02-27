#!/usr/bin/python

import requests
import sys
import threading
import Queue

rs=open('rs.txt','a')
dir_1=open('/root/dir_dict.txt').readlines()
q=Queue.Queue(maxsize=len(dir_1))
p=Queue.Queue(maxsize=1)
urls=[]
p.put(rs)

th=[]
thread_s=int(raw_input('Pleasd chose you threads!:'))

if len(sys.argv) !=1:
    for i in range(len(sys.argv)):
        if i ==0:
            continue
        url=sys.argv[1]

print url

def scan_dir(url):
    global dir_1
    global q
    global p

    if url.startswith('http://'):
        while not q.empty():
            y=q.get()
            re=requests.get(url+y)
            print url+y+'.......'
            if re.status_code==200:
                rs_1=p.get()
                rs_1.write(url+y+' :200\n')
                p.put(rs_1)
            elif re.status_code==403:
                rs_1=p.get()
                rs.write((url+y+' :403\n'))
                p.put(rs_1)

def main():
    global url
    global p
    global q

    if q.empty():
        for i in dir_1:
            q.put(i)
        for z in range(thread_s):
            th.append(threading.Thread(target=scan_dir,args=(url,)).start())

if __name__ == '__main__':
    main()

