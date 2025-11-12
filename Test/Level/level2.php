<?php
// Level 2: Unknown methods on expressions
$str = "hello";
$str->unknownMethod();

// Fixed: Use proper string functions
$str = "hello";
echo strlen($str);
?>