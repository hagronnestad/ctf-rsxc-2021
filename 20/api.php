<?php

$data = json_decode(file_get_contents('php://input'), true);

if(!isset($data['hmac']) || !isset($data['host'])) {
  header("HTTP/1.0 400 Bad Request");
  exit;
}
$secret = getenv("SECRET");
$flag = getenv("FLAG");

$hmac = hash_hmac($data["host"], $secret, "sha256");

if ($hmac != $data['hmac']){
  header("HTTP/1.0 403 Forbidden");
  exit;
}

echo $flag;
