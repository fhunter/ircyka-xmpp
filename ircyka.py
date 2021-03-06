#h!/usr/bin/python
# -*- coding: utf-8 -*-
from xmpp import *
import time,os
import sqlite3
import messages
import settings

setts=settings.get_values()
BOT=['','','']
CONF=['','']
if setts['jid'] != None:
    BOT[0]=setts['jid']
if setts['password']!=None:
    BOT[1]=setts['password'];
if setts['resource']!=None:
    BOT[2]=setts['resource'];
if setts['conference']!=None:
    CONF[0]=setts['conference']
if setts['nick']!=None:
    NICK=setts['nick']
PROXY={}

def messageCB(sess,mess):
    nick=mess.getFrom().getResource()
    text=mess.getBody()
    resp=messages.act_on_message(conn,setts,nick,text)
    for text in resp:
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
            if nick == NICK:
                text=''
            else:
                text=nick+': '+messages.get_greeting(conn)
            roster.append(nick)
    if text: cl.send(protocol.Message(CONF[0],text,'groupchat'))

if 1:
    cl=Client(JID(BOT[0]).getDomain(),debug=[])
    cl.connect(proxy=PROXY)
    conn=sqlite3.connect('base.sqlite3')
    cl.RegisterHandler('message',messageCB)
    cl.RegisterHandler('presence',presenceCB)
    cl.auth(JID(BOT[0]).getNode(),BOT[1],resource=BOT[2])
    p=Presence(to='%s/%s'%(CONF[0],NICK))
    p.setTag('x',namespace=NS_MUC).setTagData('password',CONF[1])
    p.getTag('x').addChild('history',{'maxchars':'0','maxstanzas':'0'})
    cl.send(p)
    while 1:
        cl.Process(1)
