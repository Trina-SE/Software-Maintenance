<?php
// Level 5: Argument types check
function foo(int $x) {}
foo("string");

// Fixed: Pass correct type
function foo_fixed(int $x) {}
foo_fixed(5);
?>