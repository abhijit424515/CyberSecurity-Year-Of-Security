# flag{}
from os import system, name
from sys import exit
from time import sleep
from pwn import *
from functools import reduce

def clear():
    if(name=='nt'):
        _ = system('cls')
    else:
        _ = system('clear')

#############################################

def bestmove(k,n):
    if n==1:
        if k[2]=='x':  
            yield "2,0"                 # 1st
            if k[6]=='_':
                yield "1,0W"

        if k[4]=='x':  return "2,0"                 # 3rd
        if k[6]=='x':  return "0,2"                 # 1st
        if k[8]=='x':  return "2,2"                 # 2nd
        if k[10]=='x': return "2,2"                 # 4th
        if k[12]=='x': return "2,2"                 # 3rd
        if k[14]=='x': return "2,2"                 # 4th
        if k[16]=='x': return "2,2"                 # 5th

    if n==2:
        if k[2]=='x' and k[6]=='_': return "1,0"    # 1st   # and k[12]=='o'
        if k[6]=='x' and k[2]=='_': return "0,1"    # 1st   # and k[4]=='o'
        if k[2]=='x' and k[6]=='x' and k[4]=='o' : return "2,2"    # 1st   # and k[12]=='o'
        if k[2]=='x' and k[6]=='x' and k[12]=='o': return "1,0"    # 1st   # and k[12]=='o'
        


def check_status():


p = process('./ttt')

x = []
game = 1

while game <= 10:
    # start
    x = reduce(lambda x,y: x+y,str(p.read())[2:-1].split("\\n")[3:6])
    print(x)
    p.write("0,0\n")
    n=1

    # recursive-loops
    while True:
        x = reduce(lambda x,y: x+y,str(p.read(timeout=1))[2:-1].split("\\n")[0:3])
        print(x)
        t = bestmove(x,n)
        p.write(t[0:3]+"\n")
        if len(t)>3: 
            n=1
            if t[3]=='W': 
                break
            elif t[3]=='F':
                game=0
                break
        n+=1
        # sleep(500)
    game+=1
    