#coding: utf-8
from pwn import *
import os

argv = range(100)
argv[0] = './input'
argv[ord('A')] = "\x00"
argv[ord('B')] = "\x20\x0a\x0d"
argv[ord('C')] = "8888"

cwd = "/tmp/input"

env = {"\xde\xad\xbe\xef":"\xca\xfe\xba\xbe","PWD":"/tmp/input/"}

f = open("/tmp/input/\x0a" , "wb")
f.write("\x00"*4)
f.close()

pinr,pinw = os.pipe()
perrr,perrw = os.pipe()
os.write(pinw,"\x00\x0a\x00\xff")
os.write(perrw,"\x00\x0a\x02\xff")

p = process(argv,env=env,cwd=cwd,stdin=pinr,stderr=perrr)

sleep(1) # wait for socket

so = remote("127.0.0.1", 8888)
so.send("\xde\xad\xbe\xef")

sleep(1) # wait for stdout

print so.recv()
