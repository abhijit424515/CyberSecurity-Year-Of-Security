A new modular challenge!
Download the message [here](https://artifacts.picoctf.net/c/499/message.txt).
Take each number mod 41 and find the modular inverse for the result. 
Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

---

Write python file.
```
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
```

---

```picoCTF{1NV3R53LY_H4RD_C680BDC1}```
