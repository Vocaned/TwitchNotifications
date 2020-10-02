import socket
import typing

class Socket(socket.socket):
    def __init__(self, host, password=None, nick=None, join=None):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(host)

        if password:
            self.sendPacket(f'PASS {password}')
        self.sendPacket(f'NICK {nick}')
        if join:
            if isinstance(join, str):
                self.sendPacket(f'JOIN #{join}')
            else:
                for channel in join:
                    self.sendPacket(f'JOIN #{channel}')


    def readPacket(self) -> str:
        return self.recv(2048).decode('utf-8')

    def sendPacket(self, data: str):
        print('> ' + data)
        self.sendall(data.encode('utf-8')+b'\r\n')

    def sendMessage(self, channel: str, message: str):
        self.sendall(b'PRIVMSG #%b :%b' % (channel, message))