from TwitchNotifications.config import getConfig
import json
import typing
import requests
from datetime import datetime

# First escaping python, then escaping string, then escaping json, then escaping discord = \\\\\\\\
# fucking spaghetti lol
def escape(string: str, char: typing.Union[str, list], escapeChar: str = '\\\\\\\\') -> str:
    if isinstance(char, str):
        return string.replace(char, escapeChar+char)

    for c in char:
        string = string.replace(c, escapeChar+c)
    return string

def sendNotif(channel: str, username: str, message: str):
    c = getConfig()

    print('Sending notification: ' + message)

    if c['notifOptions'] == 'escapediscord':
        message = message.replace('@everyone', '@\\\\everyone').replace('@here', '@\\\\here')
        message = escape(message, ['_', '*', '~'])

    content = c['notifContent'].replace('{channel}', channel).replace('{username}', username).replace('{time}', str(datetime.now()).split('.')[0]).replace('{message}', message)

    if c['notifType'] == 'post':
        j = json.loads(content)
        requests.post(c['notifParams'], data=j.encode('utf-8'), headers={'Content-Type': 'application/json'})