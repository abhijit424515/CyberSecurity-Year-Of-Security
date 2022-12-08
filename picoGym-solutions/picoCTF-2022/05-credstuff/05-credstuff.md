
We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
Download the leak here(https://artifacts.picoctf.net/c/534/leak.tar).
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

---

First, extract tar file using

```tar -xf leak.tar```

Write python file, which exports encrypted flag to 'enc'.
Finally, 

```cat enc | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'```

---

```picoCTF{C7r1F_54V35_71M3}```
