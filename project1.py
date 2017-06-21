#!/usr/bin/python

import  cgi,cgitb,os,time,commands,sys
cgitb.enable()
print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
user=x.getvalue('u')
password=x.getvalue('p')

if  user  ==  'root'  and  password  == 'me' :
	print  "authentication Done  redirecting to new page"
        print "<meta http-equiv='refresh' content='2;url=http://192.168.43.108/myproject/ipscan.html'/>"


else  :
	print   "bad  authentication  details !!"
	print  "<meta http-equiv='refresh' content='2;url=http://192.168.43.108/myproject/login.html'/>"
