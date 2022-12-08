Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.
Download the data [here](https://artifacts.picoctf.net/c/294/anthem.flag.txt).

---

Wget the file. Then use

```cat anthem.flag.txt | grep -Eo "picoCTF{.*}"```

## Reference for GREP REGEX => [here](https://linuxize.com/post/regular-expressions-in-grep/)
 
In the above command, -o flag shows only the searched chars, and -E flag is for extended regex usability in searching. 
The dot . means any single character.
The asterisk * means any whole number of previous character type.

---

```picoCTF{gr3p_15_@w3s0m3_4c479940}```
