#https://api.telegram.org/bot-Kendiapiniz-/sendMessage
#https://api.telegram.org/bot/getUpdates

import requests

class Telegram:
    pass
    #def __init__(self, message):
    #    self.message = message
def sendMessage(msg):
    sendUrl = "https://api.telegram.org/bot7145550:659da193100cfd421ce6aedf1ef6ea79/sendMessage"
    requests.post(url=sendUrl, data={"chat_id":"1099086328","text":"msg"})