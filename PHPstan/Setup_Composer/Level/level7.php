<?php
// Level 7: Union types issues
function foo(string|int $x) {
    $x->method();
}

// Fixed: Check type before calling method
function foo_fixed(string|int $x) {
    if (is_string($x)) {
        echo strlen($x);
    } else {
        echo $x;
    }
}
?>