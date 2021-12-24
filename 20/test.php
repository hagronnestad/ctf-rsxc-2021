<?php
$data = json_decode('{ "hmac": "", "host": "" }');
$hmac = hash_hmac($data["host"], $secret, "sha256");
var_dump($data);
var_dump($hmac);