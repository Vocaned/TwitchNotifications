from TwitchNotifications.config import getConfig
import json
import typing
import requests
from datetime import datetime

def escape(string: str, char: typing.Union[str, list], escapeChar: str = '\\') -> str:
    if isinstance(char, str):
        return string.replace(char, escapeChar+char)

    for c in char:
        string = string.replace(c, escapeChar+c)
    return string

def sendNotif(channel: str, username: str, message: str):
    c = getConfig()

    print('Sending notification: ' + message)

    content = c['notifContent'].replace('{channel}', channel).replace('{username}', username).replace('{time}', str(datetime.now()).split('.')[0]).replace('{message}', message)

    if c['notifOptions'] == 'escapediscord':
        content = content.replace('@everyone', '@\\everyone').replace('@here', '@\\here')
        content = escape(content, ['_', '*', '~'])

    if c['notifType'] == 'post':
        j = json.loads(content)
        requests.post(c['notifParams'], data=j)