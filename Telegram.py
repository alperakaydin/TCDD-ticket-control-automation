#https://api.telegram.org/bot-Kendiapiniz-/sendMessage
#https://api.telegram.org/bot/getUpdates

import requests

class Telegram:
    pass
    #def __init__(self, message):
    #    self.message = message
def sendMessage(msg):
    sendUrl = "https://api.telegram.org/********:**********/sendMessage"
    requests.post(url=sendUrl, data={"chat_id":"chat_id","text":"msg"})
