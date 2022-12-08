# flag{}
from os import system, name
from sys import exit
from time import sleep
from pwn import *

def clear():
    if(name=='nt'):
        _ = system('cls')
    else:
        _ = system('clear')

#############################################

p = process('./minesweeper')

l = []
game = 1
while game <= 10:
    # start
    x = str(p.read(timeout=1))

    # recursive-loops
    p.write("1,1\n")
    x = str(p.read(timeout=1))[2:-1].split("\\n")[0:9]
    # print(x)
    
    sleep(500)