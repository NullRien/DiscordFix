from os import path, remove, getenv
from sys import stdout, exit
from time import sleep

discord_path = path.join(getenv('APPDATA'), 'discord')

if path.exists(discord_path):
    remove(discord_path)
    print('Discord folder removed')
    for char in "You are free. Now go outside.": 
        print(char, end='') 
        stdout.flush() 
        sleep(0.1) 

if not path.exists(discord_path):
    print('Discord not found')
    exit(1)

