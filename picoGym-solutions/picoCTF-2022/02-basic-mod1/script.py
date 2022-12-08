f = open("message.txt", "r")
g = f.read()
g = g.split(" ")[0:-1]

x = ""

for i in g:
    y = int(i)%37
    if y<26:
        x+=chr(y+65)
    elif y<36:
        x+=str(y-26)
    elif y==36:
        x+="_"

print("picoCTF{"+x+"}")