<?php

class User {
    public $name;

    // $age not declare  → intentional error
    public function getAge(): int {
        return $this->age;
    }

    // Function type mismatch → intentional error
    public function addNumbers(int $a, int $b): int {
        return $a + $b;
        // @phpstan-ignore deadCode.unreachable
        $c;
    }
}

$user = new User();

$user->name = "Mostafizur";
$user->getAge();           // $age is undefined
$user->addNumbers(5, "10"); // second param is string
