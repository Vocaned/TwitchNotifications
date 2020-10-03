from TwitchNotifications.config import getConfig
import json
import requests
from datetime import datetime

def sendNotif(channel: str, username: str, message: str):
    c = getConfig()

    print('Sending notification: ' + message)

    content = c['notifContent'].replace('{channel}', channel).replace('{username}', username).replace('{time}', str(datetime.now()).split('.')[0]).replace('{message}', message)

    if c['notifOptions'] == 'escapediscord':
        content = content.replace('@everyone', '@\\everyone').replace('@here', '@\\here').replace('_', '\\_').replace('*', '\\*').replace('~', '\\~')

    if c['notifType'] == 'post':
        j = json.loads(content)
        requests.post(c['notifParams'], data=j)