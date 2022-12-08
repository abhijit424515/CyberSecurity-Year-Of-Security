stepped = open("cipher.txt", "r")
z = stepped.read().strip()
y1 = "cylab"
y2 = "CYLAB"
leng = 5

final = ""

x = 0

temp = ""

for i in z:
    if ord(i) == 95 or ord(i) == 123 or ord(i) == 125:
        temp += i
    elif ord(i) == 90:
        temp += "A"
    elif ord(i) == 122:
        temp += "a"
    elif ord(i) >= 48 and ord(i) <= 57:
        temp += i
    else:
        temp += chr(ord(i)+1) 

for i in temp:
    if ord(i) >= 65 and ord(i) <= 90 :
        checked = ord(i)-ord(y2[x%leng]) - 1
        if checked < 0:
            checked += 26
        checked += 65
    elif ord(i) >= 97 and ord(i) <= 122 :
        checked = ord(i)-ord(y1[x%leng]) - 1
        if checked < 0:
            checked += 26
        checked += 97
    elif ord(i) == 95 or ord(i) == 123 or ord(i) == 125:
        checked = ord(i)
        x -= 1
    elif ord(i) >= 48 and ord(i) <= 57:
        checked = ord(i)
        x -= 1
    final += chr(checked)
    x += 1

stepped.close()
print(final)