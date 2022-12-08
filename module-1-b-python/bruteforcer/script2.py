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
password = "a"

# seq = [str(i) for i in range(10)]+[str(chr(i)) for i in ([j for j in range(65,91)]+[j for j in range(97,123)])]

for i in range(0,10):
    seq.append(str(i))
for i in range(65,91):
    seq.append(str(chr(i)))
for i in range(97,123):
    seq.append(str(chr(i)))  

p = process("./bruteforcer")

#############################

while True:
    p.write(password+"\n")
    x = str(p.read(timeout=1))
    parity1 = x.find("too low")
    parity2 = x.find("too high")

    if (parity1==-1 and parity2==-1):
        break

    with open("wordlist.txt") as f:
        for line in f:
            while True:
                ind = 0
                seq.index(line[ind])

#############################

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