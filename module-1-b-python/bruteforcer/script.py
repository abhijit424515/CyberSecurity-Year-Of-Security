# flag{b1n42y_s3r2ch_f7w}
from os import system, name
from time import sleep
from pwn import *
import math

def clear():
    if(name=='nt'):
        _ = system('cls')
    else:
        _ = system('clear')

seq = []
password = ""

for i in range(0,10):
    seq.append(str(i))
for i in range(65,91):
    seq.append(str(chr(i)))
for i in range(97,123):
    seq.append(str(chr(i)))    

index1 = 0
index2 = 61

while True:
    p = process('./bruteforcer')

    indexM = math.floor((index1+index2)/2)
    
    if indexM==index1:
        if index1==index2:
            p.sendline(password+str(seq[index1]))
            word = str(p.recvall(timeout=1))
            if word.find("too low")!=-1:
                password+=str(seq[index1])
                # print(password)
                index1 = 0
                index2 = 61
                p.close()
                continue
            elif word.find("too high")==-1:                                 # VVI
                password+=str(seq[index1])
                break
        else:
            p.sendline(password+str(seq[index2]))
            word = str(p.recvall(timeout=1))
            if word.find("too low")!=-1:
                password+=str(seq[index2])
            elif word.find("too high")!=-1:
                password+=str(seq[index1])
            else:
                password+=str(seq[index2])
                p.close()
                break                                                       # VVI
            # print(password)
            index1 = 0
            index2 = 61
            p.close()
            continue
    else:
        p.sendline(password+str(seq[indexM]))
        temp = str(p.recvall(timeout=1))

        if(temp.find("too low")!=-1):
            index1 = indexM
        elif(temp.find("too high")!=-1):
            index2 = indexM
        else:
            p.close()
            password += str(seq[indexM])
            break
        p.close()

clear()
print("The password is", password)
sleep(2)
p = process('./bruteforcer')
p.sendline(password)
temp = str(p.recvall(timeout=1))
first = temp.index("flag{")
last = temp.index("}")
clear()
for i in range(first, last+1):
    print(temp[i],end="")
print("")