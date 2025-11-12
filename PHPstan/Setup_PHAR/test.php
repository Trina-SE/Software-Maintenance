<?php

function addNumbers(int $a, int $b): int {
    return $a + $b;
}

// This is an intentional error: passing a string instead of int
$result = addNumbers(5, "10");

echo $result;

//php phpstan.phar analyse test.php --level=5  
