<?php
// Level 0: Basic checks - unknown class
$obj = new UnknownClass();

// Fixed: Use a valid class
$obj = new stdClass();
?>