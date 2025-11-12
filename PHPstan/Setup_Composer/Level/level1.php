<?php
// Level 1: Possibly undefined vars
if (rand() > 0.5) {
    $x = 1;
}
echo $x;

// Fixed: Define variable always or check before use
$x = null;
if (rand() > 0.5) {
    $x = 1;
}
if ($x !== null) {
    echo $x;
}
?>