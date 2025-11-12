<?php
// Level 3: Return types
function foo(): int {
    return "string";
}

// Fixed: Return correct type
function foo_fixed(): int {
    return 42;
}
?>