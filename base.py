#Simple Base for Telegram BOT writed in python
#Dev Francesco666, Neon(Thanks you so much for help)

import requests,json

token = "INSER TOKEN HERE"
telegram = "https://api.telegram.org/bot"+token+"/"

def apireq(method):
    ok = requests.get(telegram+method).text
    return ok
    #Function!
def sendMessage(chatid, msg):
    jej = requests.post(telegram+"sendMessage", data={'chat_id':chatid, 'text':msg})
    return jej.text

def sendPhoto(chatid, photo, caption):
    url = "https://api.telegram.org/bot"+str(token)+"/sendPhoto?chat_id="+str(chatid)+"&caption="+str(caption)
    requests.post(url, files={'foto':photo}).text
    
def sendDocument(chatid, document, caption):
    url = "https://api.telegram.org/bot"+str(token)+"/sendDocument?chat_id="+str(chatid)+"&caption="+str(caption)
    requests.post(url, files={'document': open(document, 'rb')}).text
    
def forward(chatid, fchatid, msgid):
    requests.post(telegram+"forwardMessage", data={'chat_id':chatid, 'from_chat_id':fchatid, 'message_id':msgid})

def sendVideo(chatid, video, caption):
    url = "https://api.telegram.org/bot"+str(token)+"/sendVideo?chat_id"+str(chatid)+"&caption="+str(caption)
    requests.post(url, files={'video':video}).text

def Keyboard(chatid, keyboard, msg): #broken for now >((
    requests.post(telegram+"sendMessage", data={'chat_id':chatid, 'text':msg, 'reply_markup':keyboard}).text

def setToken(t):
    global token
    token = t

rip = []
def killup():
    rip.append(update_id)

while True:
    try:
        up = requests.get("https://api.telegram.org/bot"+token+"/getupdates?offset=-1").text
        data = json.loads(up)
        #print up 
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

    except:
        print "ERROR!"
        continue
    

