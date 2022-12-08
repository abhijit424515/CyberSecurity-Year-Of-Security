file = open("message.txt").read().strip()

i = 0

while i < len(file):
    listi = list(file) 
    listi[i+2], listi[i+1] = listi[i+1], listi[i+2]
    listi[i], listi[i+1] = listi[i+1], listi[i]
    file = ''.join(listi)
    i += 3

print(file)
