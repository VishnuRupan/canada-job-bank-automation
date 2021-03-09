from validate_email import validate_email
from getpass import getpass
import time
import os


clear = lambda: os.system('cls')

def mainHeaderPrint(keyword, name,pathname):
    clear()
    print('\n\n--- Canada Job Bank Automation ---\n----------------------------------\n')
    print('Excluded Keyword: ' + keyword + '\n')
    print('Sign off: ' + name + '\n')
    print('Pathname: ' + pathname + '\n')
    print('----------------------------------\n')

def getBeans():
    beans = getpass()
    return beans

def getUserName():
    username = str(input('Email: '))
    return username

def login_email(send_mail,pathname):
    counter = 0
    print("\nGmail Login (password hidden):\n------------------------------\n")
    username = getUserName()
    beans = getBeans()

    try:
        send_mail(username, username, 'Automation Connection Test', 'Automation Connection Test - Temp Delete', pathname, 'smtp.gmail.com', '587', username, beans)
        print('\nConnected...')
        counter = 1
        time.sleep(3)
    except:
        print('\nEmail login failed. Please try again.')
        counter = 0
        time.sleep(2)

    return counter,username,beans


def getTimeSpeed():
    speed = 0
    try:
        print('Enter the following number(1 or 2) based on your computer\'s speed: ')
        speed = int(input("\n    1. Fast\n    2. Slow\n\nEnter:  "))
        if speed == 1:
            speed = 2
        elif speed >= 2:
            speed = 4
    except:
        print('')

    return speed



def getMsg():
    msg = 0
    try:
        print('Enter the following number(1 or 2) for your email message to employers: ')
        msg = int(input("\n    1. Simple\n    2. Detailed\n\nEnter:  "))
        if msg == 1:
            msg = 1
        elif msg >= 2:
            msg = 2
    except:
        print('')

    return msg


def dontDoIt():
    msg = 0
    try:
        print('Enter the following number(1 or 2): ')
        msg = int(input("\n    1. Run both Excel & Email functions\n    2. Only Excel\n\nEnter:  "))
        if msg == 1:
            msg = 1
        elif msg >= 2:
            msg = 2
    except:
        print('')

    return msg