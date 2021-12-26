# 0x02 - A magic word

> We have found a magical port that is listening on port 20002, maybe you can find todays flag there?
> rsxc.no:20002

---

Let's `netcat` the service:

```bash
$ nc rsxc.no 20002
a
That is not the byte I want!

Ncat: Broken pipe.
```

Ok, so based on the message we can assume that the service wants us to send a certain byte.

Let's create a Python script to brute force the byte:

From `02.py`
```python
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

```

Now let's run it:

```bash
$ ./02.py

...

[+] Opening connection to rsxc.no on port 20002: Done
[*] Closed connection to rsxc.no port 20002
b'That is not the byte I want!\n'
Trying: b'\xd2'
[+] Opening connection to rsxc.no on port 20002: Done
[*] Closed connection to rsxc.no port 20002
b'That is not the byte I want!\n'
Trying: b'\xd3'
[+] Opening connection to rsxc.no on port 20002: Done
[*] Closed connection to rsxc.no port 20002
b'That is not the byte I want!\n'
Trying: b'\xd4'
[+] Opening connection to rsxc.no on port 20002: Done
[*] Closed connection to rsxc.no port 20002
b'RSXC{You_found_the_magic_byte_I_wanted_Good_job!}'
```

## Solution

The magical byte is `0xd4` and the flag is `RSXC{You_found_the_magic_byte_I_wanted_Good_job!}`.