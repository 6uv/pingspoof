import requests
from colorama import Fore, init
import os
init(convert=True)

intro = """
                    Made by REZIZT. I already know your skidding this just admit it
                            Discord : https://discord.gg/XgpXMWk2bG
                 ██▓███   ██▓ ███▄    █   ▄████   ██████  ██▓███   ▒█████   ▒█████    █████▒
                ▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▒██    ▒ ▓██░  ██▒▒██▒  ██▒▒██▒  ██▒▓██   ▒ 
                ▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒██░  ██▒▒████ ░ 
                ▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓  ▒   ██▒▒██▄█▓▒ ▒▒██   ██░▒██   ██░░▓█▒  ░ 
                ▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒▒██████▒▒▒██▒ ░  ░░ ████▓▒░░ ████▓▒░░▒█░    
                ▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ░    
                ░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░ ░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░   ░ ▒ ▒░  ░      
                ░░        ▒ ░   ░   ░ ░ ░ ░   ░ ░  ░  ░  ░░       ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░    
                          ░           ░       ░       ░               ░ ░      ░ ░          
                                                                                         


                                            [+]1 Ping spoof
                                            [+]2 Everyone spoof
"""

def ping():
    print(f'[{Fore.RED}>{Fore.RESET}] Your token', end=''); token = str(input('  :  '))
    print(f'[{Fore.RED}>{Fore.RESET}] Channel id', end=''); channel = str(input('  :  '))
    print(f'[{Fore.RED}>{Fore.RESET}] Users ID to ping', end=''); user = str(input('  :  '))
    headers = {'Authorization': token}
    print('Sending message...')
    message = f'<@{user}>'
    requests.post(f'https://discordapp.com/api/v6/channels/{channel}/messages', headers=headers, json={'content':message, 'tts': False, 'nonce': None, 'allowed_mentions': {'everyone': True, user: True, 'member': True }})
    print('Message sent!')
    startMenu()

def everyone():
    print(f'[{Fore.RED}>{Fore.RESET}] Your token', end=''); token = str(input('  :  '))
    print(f'[{Fore.RED}>{Fore.RESET}] Channel id', end=''); channel = str(input('  :  '))
    headers = {'Authorization': token}
    print('Sending message...')
    message = f'hey @everyone'
    requests.post(f'https://discordapp.com/api/v6/channels/{channel}/messages', headers=headers, json={'content':message, 'tts': False, 'nonce': None, 'allowed_mentions': {'everyone': True, 'member': True }})
    print('Message sent!')
    startMenu()

def startMenu():
    print(intro)
    print(f'[{Fore.RED}>{Fore.RESET}] Your choice', end=''); choice = str(input('  :  '))
    if choice == '1':
       os.system('cls')
       ping()

    elif choice == '2':
        os.system('cls')
        everyone()

if __name__ == '__main__':
    startMenu()