f = open("message.txt", "r")
g = f.read()
g = g.split(" ")[0:-1]

x = ""

for i in g:
    z = int(i)%41
    y=0
    for j in range(1,41):
        if (j*z)%41==1:
                y = j
                break
    if y<27:
        x+=chr(y+64)
    elif y<37:
        x+=str(y-27)
    elif y==37:
        x+="_"

print("picoCTF{"+x+"}")
