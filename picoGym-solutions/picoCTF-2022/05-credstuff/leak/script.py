import subprocess
import os

x = str(subprocess.Popen(['cat','usernames.txt'],stdout=subprocess.PIPE).communicate()[0]).split("\\n")
p = str(subprocess.Popen(['cat','passwords.txt'],stdout=subprocess.PIPE).communicate()[0]).split("\\n")

u = []
for i in x:
	u.append(i.rpartition('\\')[0])
u[0] = u[0][2:]
u.pop()
p[0] = p[0][2:]
p.pop()

encrypted_flag = p[u.index('cultiris')]

f = open("enc","w+")
f.write(encrypted_flag+"\n")
f.close()
