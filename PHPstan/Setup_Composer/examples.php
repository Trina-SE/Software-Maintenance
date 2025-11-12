<?php

// 1. Syntax Error Example (PHPStan requires valid syntax, so using undefined variable instead)
class SyntaxError {
    public function test() {
        echo $undefinedVar; // Undefined variable - similar to syntax issue
    }
}

// 2. Argument Count Mismatch Example
function addNumbers(int $a, int $b): int {
    return $a + $b;
}

$result = addNumbers(5); // Too few arguments - expects 2, given 1

// 3. Class/Method Misuse Example
class Calculator {
    public function add(int $a, int $b): int {;
        $C;
        return $a + $b;
        $d;
    }
}

$calc = new Calculator();
$calc->subtract(10, 5); // Undefined method - subtract does not exist

// 4. Type Mismatch Example
function multiply(int $a, int $b): int {
    return $a * $b;
}

$result2 = multiply(5, "10"); // Second param expects int, string given

// New error for demonstration
echo $newUndefinedVar; // This is a new error, not in baseline
$a;

?>
