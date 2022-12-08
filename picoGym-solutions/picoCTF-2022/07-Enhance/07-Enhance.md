Download [this](https://artifacts.picoctf.net/c/136/drawing.flag.svg) image file and find the flag.

---

On analysing the SVG file, we see that the flag is broken down and printed by tspan tag
So, we use
```cat drawing.flag.svg | grep tspan```

---

```picoCTF{3nh4nc3d_aab729dd}```
