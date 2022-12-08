Can you get the flag?
Download this [binary](https://artifacts.picoctf.net/c/115/gdbme).
Here's the test drive instructions:
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)

---

GDB is the GNU Debugger, which allows us to see what's going on in the registry values,memory,stack,heap,etc while a program runs.
We set a break point at *(main+99), and jjumped the code execution to *(main_104), which couted the flag.

---

```picoCTF{d3bugg3r_dr1v3_197c378a}```
