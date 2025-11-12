<?php
// Level 9: Strict mixed
function foo(mixed $x) {
    $x->method();
}

// Fixed: Check type
function foo_fixed(mixed $x) {
    if (is_object($x)) {
        $x->method();
    }
}
?>