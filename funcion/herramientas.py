import os

def clrScr():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
