#!/usr/bin/python3

from pwn import *

def try_byte(bytes):
	conn = remote('rsxc.no', 20002)
	conn.send(bytes);
	r = conn.recv()
	conn.close()
	
	print(r)

	if r == b'That is not the byte I want!\n':
		return False

	return True

for x in range(200, 256):
	print(f"Trying: {p8(x)}")
	r = try_byte(p8(x))
	if r: break
