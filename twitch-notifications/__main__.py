from sock import Socket
socket = Socket(('irc.twitch.tv', 6667), password='asd', nick='Fam0r', join='fam0r')

if __name__ == "__main__":
    while True:
        data = socket.readPacket()
        if not data: continue

        for message in data.split('\r\n'):
            msgtype = message.split(' ')[0]
            
            if msgtype == 'PING':
                socket.sendPacket(message.replace('PING', 'PONG'))
            elif msgtype == 'PRIVMSG':
                username = data.split('!')[0].lstrip(':')
                message = ' '.join(message.split()[4:])[1:]

                print(username, message)