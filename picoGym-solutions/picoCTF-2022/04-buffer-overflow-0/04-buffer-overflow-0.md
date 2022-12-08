Smash the stack
Let's start off simple, can you overflow the correct buffer? T
he program is available here(https://artifacts.picoctf.net/c/520/vuln). 
You can view source here(https://artifacts.picoctf.net/c/520/vuln.c). 

And connect with it using:
```nc saturn.picoctf.net 53935```

---

On analysing the code, the flag will be printed when sigsev_handler() is called.
The signal function is called when there is a system call to SIGSEGV, which is an error denoting segmentation fault/violation.

So basically, if we input something to cause a segmentation fault, the flag will get printed.
Since gets is used to send our input to buf1, which has max character limit of 100, we must write some text/number of length > 100.
Also, the vuln function copies the input string buf1 to buf2, which has max character limit of 16. So, text of length > 16 may work.
Since some other variable may be using the locations > 16 indices of array, we have to try using a big number like 20,30 or something.

---

```picoCTF{ov3rfl0ws_ar3nt_that_bad_a065d5d9}```
