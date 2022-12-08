We found this weird message being passed around on the servers, we think we have a working decryption scheme. 
Download the message [here](https://artifacts.picoctf.net/c/393/message.txt). 
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

---

Write python code. [[script.py]]
```python
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
```

---
```picoCTF{R0UND_N_R0UND_79C18FB3}```

