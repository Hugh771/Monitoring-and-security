#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import urllib
import random


def spider():
    num=0
    page_num=255
    for i in range(0,30):
        url='http://jandan.net/ooxx/page-'+str(page_num)+'#comments'
        page_num -= 1
        r=requests.get(url,verify=False)
        bs=BeautifulSoup(r.text,'lxml')
        img_list=bs.find_all('img')
        for img in img_list:
            if img.attrs['src']:
                num+=1
                spidef_img(img.attrs['src'],num)
            else:
                continue

def spidef_img(url_img,img_num):
    if not url_img.startswith('http:'):
        url_img='http:'+url_img
        if not url_img.endswith('jpg'):
            return 0

    print 'img dowlod'
    urllib.urlretrieve(url_img,'/root/jandanimg/new/'+str(img_num)+'.jpg')

if __name__ == '__main__':
    spider()
