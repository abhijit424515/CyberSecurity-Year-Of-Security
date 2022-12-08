Download the packet capture file [here](https://artifacts.picoctf.net/c/199/network-dump.flag.pcap) and use packet analysis software to find the flag.

---

Open the file with Wireshark, and Follow the TCP stream of the [psh,awk] request.
The flag was sent in that packet.

Or, we can use
```strings network-dump.flag.pcap | grep "p i c o C T F" | tr -d " "```

---

```picoCTF{p4ck37_5h4rk_ceccaa7f}```
