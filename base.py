#!/usr/bin/env python2
#Simple Base for Telegram BOT wrote in python
#Dev Francesco666, Neon(Thank you so much for help)
'''
TODO:
-Fix inline keyboard
'''
import requests
import json

token = "INSERT TOKEN HERE"
apiurl = "https://api.telegram.org/bot" + token + "/"

def apirequest(method, data = None):
    global apiurl
    return json.loads(requests.get(apiurl + method, data).text)    

def sendMessage(chatid, msg):
    return apirequest('sendMessage', {'chat_id': str(chatid), 'text': unicode(msg)})

def sendPhoto(chatid, photo, caption = None):
    with open(photo, 'r') as photofile:
        if caption:
            return apirequest('sendPhoto', {'photo': photofile.read(), 'chat_id': str(chatid), 'caption': unicode(caption)})
        else:
            return apirequest('sendPhoto', {'photo': photofile.read(), 'chat_id': str(chatid)})
    
def sendDocument(chatid, document, caption = None):
    with open(document, 'r') as docfile:
        if caption:
            return apirequest('sendDocument', {'document': docfile.read(), 'chat_id': str(chatid), 'caption': unicode(caption)})
        else:
            return apirequest('sendDocument', {'document': docfile.read(), 'chat_id': str(chatid)})
    
def forward(chatid, fchatid, msgid):
    return apirequest('forwardMessage', {'chat_id': chatid, 'from_chat_id': fchatid, 'message_id': msgid})

def sendVideo(chatid, video, caption = None):
    with open(video, 'r') as vidfile:
        if caption:
            return apirequest('sendVideo', {'video': vidfile.read(), 'chat_id': str(chatid), 'caption': unicode(caption)})
        else:
            return apirequest('sendVideo', {'video': vidfile.read(), 'chat_id': str(chatid)})
'''
----BROKEN----
def Keyboard(chatid, keyboard, msg):
    requests.post(telegram+"sendMessage", data={'chat_id':chatid, 'text':msg, 'reply_markup':keyboard}).text
'''

deadupdates = []
def killupdate(updid):
    global rip
    deadupdates.append(updid)

while True:
    try:
        data = apirequest('getUpdates', {'offset': '-1'})
        update = data["result"][0]
        message = update["message"]
        update_id = update["update_id"]
        text = message["text"]
        uid = message["from"]["id"]
        first = message["from"]["first_name"]
        username = message["from"]["username"]
        cid = ""
        msgid = message["message_id"]
        #ChatID
        if message["chat"]["type"] == "private":
            cid = uid    
        else:
            cid = message["chat"]["id"]
        if deadupdates not in rip:
            with open('cmd.py') as f: 
                exec(f.read())
            killupdate(update_id)

    except Exception as ex:
        print "ERROR: " + str(ex)
        continue
    

