import os
import json
import re
import config
from notification import sendNotif
from sock import Socket

if __name__ == "__main__":
    c = config.getConfig()

    socket = Socket(('irc.twitch.tv', 6667), password=c['password'], nick=c['username'], join=c['channels'])
    while True:
        data = socket.readPacket()
        if not data: continue

        for message in data.split('\r\n'):
            if not message:
                continue
            print('< ' + message)
            msg = message.split(' ')

            if msg[0] == 'PING':
                socket.sendPacket('PONG ' + msg[1])
            elif msg[1] == 'PRIVMSG':
                channel = data.split('#')[1].split(' :')[0]
                username = data.split('!')[0].lstrip(':')
                message = ':'.join(message.split(':')[2:])

                if message.startswith('\x01'):
                    message = message.replace('\x01ACTION', '/me').replace('\x01', '')

                if channel in c['channelNotifs']:
                    sendNotif(channel, username, message)
                    continue

                for regex in c['regexNotifs']:
                    if re.search(regex, message):
                        sendNotif(channel, username, message)
                        continue