<?php
// Level 10: Implicit mixed
function foo($x) {
    $x->method();
}

// Fixed: Add typehint and check
function foo_fixed(object $x) {
    $x->method();
}
?>