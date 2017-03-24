#Simple Base for Telegram BOT writed in python
#Dev Francesco666, Neon(Thanks you so much for help)

import requests,json

token = "INSERT YOUR TOKEN HERE"
telegram = "https://api.telegram.org/bot"+token+"/"

def apireq(method):
    ok = requests.get(telegram+method).text
    return ok

def sm(chatid, msg):
    sm = apireq("sendmessage?chat_id="+str(chatid)+"&text="+str(msg)+"&parse_mode=Markdown")
    return sm

rip = []

def killup():
    rip.append(update_id)

while True:
    up = requests.get("https://api.telegram.org/bot"+token+"/getupdates?offset=-1").text
    data = json.loads(up)
    #print up    IF YOU WANT TO PRINT UPDATE ON THE SCREEN DELETE THE "#" near "print up"
    #tg var
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

        
    if update_id in rip:
        continue;
    else:
            with open('cmd.py') as f: 
                s = f.read() 
                exec(s)
            killup()


    

