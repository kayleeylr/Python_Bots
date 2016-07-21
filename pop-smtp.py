#!/usr/bin/python
#-*- coding: UFT-8 -*-


from smtplib import SMTP
from poplib import POP3
from time import sleep


SMTPSVR='smtp.python.is.cool'
POP3SVR='pop.python.is.cool'

origHdrs = ['From:            ','to:    ','subject: ']
origBody = ['xxx','yyy','zzz' ]
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail('from@python.com',('to@python.com',), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('wesley')
recvSvr.pass_('youllNeverGuess')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])

sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody
