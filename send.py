#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import email.utils

class My_stmp:
    
    def __init__(self, recviver):
           self.rece = recviver  # 接收邮件
           self.server = "smtp.mailgun.org"  #设置服务器
           self.user = "ru@raydina.me"     #用户名
           self.passwd = "823264073"   #口令 
    
    def run(self):
           message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
           message['From'] = Header(u"忠告<%s>" %self.user)
           message['To'] =  Header(u"用户 <%s>" % self.rece)
           subject = 'Python SMTP 邮件测试'
           message['Subject'] = Header(subject, 'utf-8')
           try:
               smtpObj = smtplib.SMTP() 
               smtpObj.connect(self.server, 25)    # 25 为 SMTP 端口号
               smtpObj.login(self.user,self.passwd)  
               smtpObj.sendmail(self.user,  self.rece, message.as_string())
               print "邮件发送成功"
           except smtplib.SMTPException:
               print "Error: 无法发送邮件"
      
if __name__ == '__main__':
    a= My_stmp(raw_input())
    a.run()    
 
