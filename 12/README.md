# 12 - Twelve seconds of encoding

> For this challenge you need to do some encoding, but remember, you need to do it quickly, before the time runs out.
> 
> rsxc.no:20012

---

Let's `nc` into the service:

```bash
$ nc rsxc.no 20012
Good luck, you have 12 seconds to solve these 100 tasks!
Please reverse this string for me: xJBpBt
No match

$ nc rsxc.no 20012
Good luck, you have 12 seconds to solve these 100 tasks!
Please turn this to lower case for me: GYJCPLDBP
No match

$ nc rsxc.no 20012
Good luck, you have 12 seconds to solve these 100 tasks!
Can you please hex decode this for me: 5249796e577450
No match
```

Ok, so we need to do different challenges and we need to do them fast. We can see three different types of challenges above, so we need to support them all and possibly even more types. We need to create a script that can automate this for us.

Let's use `pwntools` to create a `python`-template for us:

```bash
$ pwn template --host rsxc.no --port 20012 --quiet > solve.py
```

Our script talks to the service. We receive the different types of challenges, solve them and then we send the answer back.

Here's the interesting part of our script:

```python
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
```

Let's run our script:

```bash
$ ./solve.py
[+] Opening connection to rsxc.no on port 20012: Done
b'Good luck, you have 12 seconds to solve these 100 tasks!\n'
Starting to solve chellenges...


Base64 decoding: R3dFUFFtb1RNYQ==
Result: b'GwEPQmoTMa'


Base64 decoding: WmNUT0lWc3hMUW8=
Result: b'ZcTOIVsxLQo'

Hex decoding: 574574566176
Result: WEtVav

# ... abbreviated

Hex decoding: 6b6c78426e73
Result: klxBns


Base64 decoding: eXBvUkhw
Result: b'ypoRHp'


Converting to lower case: IADOUHIRGB
Result: iadouhirgb


FLAG RECEIVED: b'RSXC{Seems_like_you_have_a_knack_for_encoding_and_talking_to_servers!}'

[*] Closed connection to rsxc.no port 20012
```



## Solution

The flag is: `RSXC{Seems_like_you_have_a_knack_for_encoding_and_talking_to_servers!}`
