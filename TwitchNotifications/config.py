import json
import os

# notifContent supports following tokens:
# {username} = Replaced with message's sender
# {message}  = Replaced with message that triggered notification
# {channel}  = Replaced with the channel where the message was sent
# {time}     = Replaced with current time

def makeConfig():
    logininfo = input('Login info (https://chatterino.com/client_login): ')
    password = 'oauth:' + logininfo.split('oauth_token=')[1].split(';')[0]
    username = logininfo.split('username=')[1].split(';')[0]
    channels = input('Join channels (comma seperated): ').replace('#', '').replace(' ', '').split(',')

    channelNotifs = input('Channel notifications\n(Sends a notification for all messages sent in channel, comma seperated): ').replace('#', '').replace(' ', '').split(',')

    regexNotifs = input('Regex notifications (seperated by ||): ').split('||')

    notifType = input('Notification type (possible values: Discord, POST): ').lower()
    if notifType == 'post':
        notifParams = input('HTTP POST URL: ')

        notifContent = '''[{time}] {username}: {message}'''

    elif notifType == 'discord':
        notifType = 'post'
        notifParams = input('Discord webhook URL: ')

        notifContent = '''{
"content": "`{time}`\\n[**{username}**@{channel}] {message}"
}'''
    else:
        print('Invalid notification type. Aborting.')
        exit(1)

    j = json.dumps({'password': password, 'username': username, 'channels': channels, 'channelNotifs': channelNotifs, 'regexNotifs': regexNotifs, 'notifType': notifType, 'notifParams': notifParams, 'notifContent': notifContent})
    with open(os.path.join(os.path.expanduser('~'), 'twitchnotifications.conf'), 'w') as f:
        f.write(j)

def getConfig() -> dict:
    if not os.path.exists(os.path.join(os.path.expanduser('~'), 'twitchnotifications.conf')):
        makeConfig()

    with open(os.path.join(os.path.expanduser('~'), 'twitchnotifications.conf')) as f:
            return json.loads(f.read())