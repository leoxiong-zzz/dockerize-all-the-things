from socket import socket


class IrcC:
    def __init__(self, host, port, channel):
        self.host = host
        self.port = port
        self.channel = channel

        self.sock = socket()
        self.conn = self.sock.makefile('rw', encoding='utf-8')

    def _loop(self):
        while True:
            raw = self.conn.readline()
            if not raw:
                break
            print('<< {}'.format(raw), end='')
            if raw.startswith('PING'):
                self.send('PONG')
            elif 'PRIVMSG' in raw:
                left, msg = raw.rsplit(':', 1)
                if 'docker' in msg.lower():
                    self.send('PRIVMSG {} :DOCKERIZE ALL THE THINGS!!!!!!!11!!@'.format(self.channel))

    def connect(self):
        self.sock.connect((self.host, self.port))

        self.send('NICK nostalgic_horse')
        self.send('USER nostalgic_horse * * nostalgic_horse')
        self.send('JOIN {}'.format(self.channel))

        self._loop()

    def send(self, data):
        self.sock.send(bytes(data + '\r\n', 'utf-8'))
        print('>> {}'.format(data))


IrcC('irc.freenode.net', 6667, '#dockerizeallthethings').connect()
