

from pwn import *

s = ssh(host='pwnable.kr',user = 'col', password='guest', port = 2222)
str = p32(0x01010101)*4+p32(0x1dd905e8)
p = s.process(argv=['./fd', str],executable='./col')
p.interactive()
