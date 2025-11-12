<?php
// Level 6: Missing typehints
function foo($x) {}

// Fixed: Add typehint
function foo_fixed(int $x) {}
?>