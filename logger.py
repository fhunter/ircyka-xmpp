#!/usr/bin/python
# -*- coding: utf-8 -*-
from xmpp import *
import time,os
import sqlite3
import greeting

BOT=('ircyka@rnet.ru','somestupidpassword')
CONF=('fishbay@conference.rnet.ru','')
LOGDIR='./'
PROXY={}

def messageCB(sess,mess):
    nick=mess.getFrom().getResource()
    text=mess.getBody()
    if 'ircyka' in text and nick!='ircyka':
        text=unicode('не грузи меня, я не сухогруз! я танкер, налей мне!','utf8');
        cl.send(protocol.Message(CONF[0],text,"groupchat"))

roster=[]
def presenceCB(sess,pres):
    nick=pres.getFrom().getResource()
    text=''
    if pres.getType()=='unavailable':
        if nick in roster:
            roster.remove(nick)
    else:
        if nick not in roster:
            if nick == 'ircyka':
                text=''
            else:
                text=nick+': '+greeting.get_greeting(conn)
            roster.append(nick)
    if text: cl.send(protocol.Message(CONF[0],text,'groupchat'))

if 1:
    cl=Client(JID(BOT[0]).getDomain(),debug=[])
    cl.connect(proxy=PROXY)
    conn=sqlite3.connect('base.sqlite3')
    cl.RegisterHandler('message',messageCB)
    cl.RegisterHandler('presence',presenceCB)
    cl.auth(JID(BOT[0]).getNode(),BOT[1])
    p=Presence(to='%s/ircyka'%CONF[0])
    p.setTag('x',namespace=NS_MUC).setTagData('password',CONF[1])
    p.getTag('x').addChild('history',{'maxchars':'0','maxstanzas':'0'})
    cl.send(p)
    while 1:
        cl.Process(1)
