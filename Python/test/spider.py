#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import urllib
import random

def spider():
    num=0
    for i in range(0,30):
        url='http://jandan.net/ooxx/page-'+str(int(2424-num))+'#comments'
        r=requests.get(url)
        bs=BeautifulSoup(r.text,'lxml')
        img_list=bs.find_all('img')
        for img in img_list:
            num+=1
            spidef_img(img.attrs['src'],num)


def spidef_img(url_img,img_num):
    if not url_img.startswith('http:'):
        url_img='http:'+url_img
    elif url_img.endswith('png'):
        return 0
    print 'img dowlod'
    urllib.urlretrieve(url_img,'/root/jandanimg/'+str(img_num)+'.jpg')

if __name__ == '__main__':
    spider()