# 0x01 - The search

> Welcome to the River Security XMas Challenge (RSXC)! RSXC operates with the following flag format for most challenges 'RSXC{flag}'. If another flag format is used, the challenge text will mention this.
> 
> In this first challenge we have managed to forget which port we are listening on. Could you please find the port listening for traffic? We know it's in the range 30 000-31 000.

---

Let's use `nmap` to find the open port between `30 000` and `31 000`.

```
nmap -p30000-31000 rsxc.no
Starting Nmap 7.70 ( https://nmap.org ) at 2021-12-01 14:22 W. Europe Standard Time
Nmap scan report for rsxc.no (134.209.137.128)
Host is up (0.035s latency).
Not shown: 1000 closed ports
PORT      STATE SERVICE
30780/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 12.87 seconds
```

Ok, we found an open port; `30780`. Let's `netcat` the port:

```
$ nc rsxc.no 30780
RSXC{Congrats!You_found_the_secret_port_I_was_trying_to_hide!}
```

## Solution

The flag is `RSXC{Congrats!You_found_the_secret_port_I_was_trying_to_hide!}`.