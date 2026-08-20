import os
import platform

def clear():
    OS = platform.system()
    if OS == "Windows": 
        os.system("cls")
    else:
        os.system("clear")