# flag{}
from os import system, name
from sys import exit
from time import sleep
from pwn import *
import math

def printer(temp,seq):
    temp = str(p.read(timeout=1))[2:-1].split("\\n")
    while (len(temp)==0):
        temp = str(p.read(timeout=1))[2:-1].split("\\n")
    if(temp[0].find("Game")!=-1):
        temp.pop(0)
        print("\n\n\n\n\n",len(temp),"\n\n\n\n\n")
    if(temp[3].find("Enter")==-1) and len(temp[4])!=0:
        print("\n\n\nThe Q is fucked\n\n\n")
    if temp == ['']:
        print("WhyTF is temp EMPTY ?")
    try:
        if(len(temp[0])!=6):
            seq = temp[1]+temp[2]+temp[3]    
        else:
            seq = temp[0]+temp[1]+temp[2]    
    except:
        for i in enumerate(temp):
            print(i[0],"\t\t",i[1])    
    for i in enumerate(temp):
        print(i[0],"\t\t",i[1])
    return temp, seq

def clear():
    if(name=='nt'):
        _ = system('cls')
    else:
        _ = system('clear')

#############################################

p = process('./ttt')

# temp = str(p.read(timeout=1))[2:-1].split("\\n")
# seq = temp[3]+temp[4]+temp[5]
# for i in enumerate(temp):
#     print(i[0],"\t\t",i[1])

while True:
    # first step
    temp = str(p.read(timeout=1))[2:-1].split("\\n")
    while (len(temp)==0):
        temp = str(p.read(timeout=1))[2:-1].split("\\n")
    try:
        seq = temp[3]+temp[4]+temp[5]
    except:
        try:
            seq = temp[0]+temp[1]+temp[2]
        except:
            print(temp)
    for i in enumerate(temp):
        print(i[0],"\t\t",i[1])
    p.write("0,0\n")
    temp,seq = printer(temp,seq)
    
    # second step
    if seq[2]=="x" or seq[4] == "x" or seq[10]=="x":
        p.write("2,0\n")
    elif seq[6]=="x" or seq[12] == "x" or seq[14]=="x":
        p.write("0,2\n")
    elif seq[16]=="x":
        p.write("2,0\n")
    elif seq[8]=="x":
        p.write("0,2\n")
        temp,seq = printer(temp,seq)
        if seq[2]=="_":
            p.write("0,1\n")
        else:
            p.write("2,1\n")
            temp,seq = printer(temp,seq)
            if seq[6]=="x":
                p.write("1,2\n")
                temp,seq = printer(temp,seq)
                if seq[16]=="_":
                    p.write("2,2\n")                                    # win
                    continue
                else:
                    p.write("2,0\n")                                    # draw
                    print("A DRAW HERE")
            elif seq[10]=="x":
                p.write("1,0\n")
                temp,seq = printer(temp,seq)
                if seq[12]=="_":
                    p.write("2,0\n")                                    # win
                    continue
                else:
                    p.write("2,2\n")                                    # draw
                    print("A DRAW HERE")
            elif seq[12]=="x" or seq[16]=="x":
                print("FUCK OFF")
                # temp,seq = printer(temp,seq)
                exit()            
    else:
        print("Failed error 001")
        temp,seq = printer(temp,seq)
        # print(temp)
        exit()
    temp,seq = printer(temp,seq)

    # third+ steps
    if seq[4]=="o" and seq[2]=="_":                                     # win
        p.write("0,1\n")
        continue                                                
    elif seq[12]=="o" and seq[6]=="_":                                  # win
        p.write("1,0\n")                                                
        continue                                                
    elif seq[4]=="o" and seq[2]=="x" and seq[8]=="_":                   # win
        if seq[6]=="x":
            p.write("1,1\n")
            temp,seq = printer(temp,seq)
            if seq[12]=="x" and seq[16]=="_":
                p.write("2,2\n")
            elif seq[12]=="_" and seq[16]=="x":
                p.write("2,0\n")
        elif seq[12]=="x":
            p.write("2,2\n")
            temp,seq = printer(temp,seq)
            if seq[10]=="x" and seq[8]=="_":
                p.write("1,1\n")
            elif seq[10]=="_" and seq[8]=="x":
                p.write("1,2\n")
        elif seq[14]=="x":
            p.write("1,1\n")                    
            temp,seq = printer(temp,seq)
            if seq[16]=="x" and seq[12]=="_":
                p.write("2,0\n")
            elif seq[16]=="_" and seq[12]=="x":
                p.write("2,2\n")
        elif seq[16]=="x":
            p.write("2,0\n")
            temp,seq = printer(temp,seq)
            if seq[6]=="x" and seq[8]=="_":
                p.write("1,1\n")
            elif seq[6]=="_" and seq[8]=="x":
                p.write("1,0\n")
        continue                                                
    elif seq[12]=="o" and seq[6]=="x" and seq[8]=="_":                  # win
        if seq[2]=="x":
            p.write("1,1\n")
            temp,seq = printer(temp,seq)
            if seq[4]=="x" and seq[16]=="_":
                p.write("2,2\n")
            elif seq[4]=="_" and seq[16]=="x":
                p.write("0,2\n")
        elif seq[4]=="x":
            p.write("2,2\n")
            temp,seq = printer(temp,seq)
            if seq[14]=="x" and seq[8]=="_":
                p.write("1,1\n")
            elif seq[14]=="_" and seq[8]=="x":
                p.write("2,1\n")
        elif seq[10]=="x":
            p.write("1,1\n")                    
            temp,seq = printer(temp,seq)
            if seq[16]=="x" and seq[4]=="_":
                p.write("0,2\n")
            elif seq[16]=="_" and seq[4]=="x":
                p.write("2,2\n")
        elif seq[16]=="x":
            p.write("0,2\n")
            temp,seq = printer(temp,seq)
            if seq[2]=="x" and seq[8]=="_":
                p.write("1,1\n")
            elif seq[2]=="_" and seq[8]=="x":
                p.write("0,1\n")
        continue                                                
    # else:
    #     print("Failed error 002")
    #     exit()
    # temp,seq = printer(temp,seq)
    
    # if len(temp)!=6:
    #     print("LAST POINT")
    #     print(temp)
    #     break

    