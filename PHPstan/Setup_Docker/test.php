<?php

function addNumbers(int $a, int $b): int {
    return $a + $b;
}

// This is an intentional error: passing a string instead of int
$result = addNumbers(5, "10");

echo $result;

//docker run --rm -v ${PWD}:/app ghcr.io/phpstan/phpstan:2-php8.2 analyse /app/test.php --level=5