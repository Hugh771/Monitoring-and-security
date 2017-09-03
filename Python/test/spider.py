#!/usr/bin/python

import requests
from bs4 import BeautifulSoup


def spider():
    num = 0
    r=requests.get('https://jandan.net/ooxx',verify=False)
    bs=BeautifulSoup(r.text,'lxml')
    img_list=bs.find_all('img')
    for img in img_list:
        if img.attrs['src']:
            num+=1
            spidef_img(img.attrs['src'],num)
    page_next=bs.find('a',title='Older Comments')

    for i in range(0,30):
        print page_next.attrs['href']
        url=page_next.attrs['href']
        r=requests.get(url,verify=False)
        bs=BeautifulSoup(r.text,'lxml')
        img_list=bs.find_all('img')
        for img in img_list:
            if img.attrs['src']:
                num+=1
                spidef_img(img.attrs['src'],num)
            else:
                continue
        page_next=bs.find('a',title='Older Comments')

def spidef_img(url_img,img_num):
    if not url_img.startswith('http:'):
        url_img='http:'+url_img
    if url_img.endswith('jpg'):
        img_postfix='.jpg'
    else:
        img_postfix='.gif'

    print 'img dowlod!!!!'
    r_img=requests.get(url_img)
    if r_img.status_code == 200:
        f=open('/root/jandan/'+str(img_num)+img_postfix,'wb')
        f.write(r_img.content)
        f.close()

if __name__ == '__main__':
    spider()
