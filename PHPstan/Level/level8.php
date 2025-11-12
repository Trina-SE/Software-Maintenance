<?php
// Level 8: Nullable types
function foo(?string $x) {
    $x->length();
}

// Fixed: Check for null
function foo_fixed(?string $x) {
    if ($x !== null) {
        echo strlen($x);
    }
}
?>