#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

context.update(arch='i386')
exe = './path/to/binary'

host = args.HOST or 'rsxc.no'
port = int(args.PORT or 20012)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

# -- Exploit goes here --

io = start()

# Receive banner
print(io.recvline())

# Solve challenges
print("Starting to solve chellenges...")

while (1):
    print("\n")

    line = io.recvline(False, 1)

    if (line.startswith(b"Please reverse this string for me: ")):
        value = line.rsplit(b": ")[1].decode()
        print(f"Reversing: {value}")
        res = value[::-1]
        print(f"Result: {res}")
        io.sendline(res)

    elif (line.startswith(b"Please base64 decode this for me: ")):
        value = line.rsplit(b": ")[1].decode()
        print(f"Base64 decoding: {value}")
        res = base64.b64decode(value)
        print(f"Result: {res}")
        io.sendline(res)

    elif (line.startswith(b"Can you please hex decode this for me: ")):
        value = line.rsplit(b": ")[1].decode()
        print(f"Hex decoding: {value}")
        res = bytes.fromhex(value).decode('utf-8')
        print(f"Result: {res}")
        io.sendline(res)

    elif (line.startswith(b"Please turn this to lower case for me: ")):
        value = line.rsplit(b": ")[1].decode()
        print(f"Converting to lower case: {value}")
        res = value.lower()
        print(f"Result: {res}")
        io.sendline(res)
    
    elif (line.startswith(b"RSXC{")):
        print(f"FLAG RECEIVED: {line}")

    else:
        print(f"Challenge not supported: {line}")

io.interactive()
