<?php
/**
 * Script to store URLs submitted via bookmarklet
 *
 * @copyright (c) 2023 ot2i7ba
 * @license MIT License
 */

// Starting session
session_start();

// Path to text and lock file
$file = 'favorites.txt';
$lockFile = 'favorites.lock';

// Check if the file exists and create it if necessary
if (!file_exists($file)) {
    file_put_contents($file, '');
    chmod($file, 0600);
}

// Check if the lock file exists and create it if necessary
if (!file_exists($lockFile)) {
    file_put_contents($lockFile, '');
    chmod($lockFile, 0600);
}

// Verify that the script was called from the bookmarklet
if (isset($_GET['url'])) {
    // Get URL from bookmarklet and filter invalid characters
    $url = filter_var($_GET['url'], FILTER_SANITIZE_URL);

    // Verify that the URL is valid and does not exceed the maximum length of 2048 characters
    if (preg_match('/^https?:\/\/[^\s\/$.?#].[^\s]*$/i', $url) && strlen($url) <= 2048) {
        // Open the lock file in write mode and lock the file
        $lockHandle = fopen($lockFile, 'r');
        flock($lockHandle, LOCK_EX);

        // Check if the URL already exists in the text file
        $favorites = file($file, FILE_IGNORE_NEW_LINES);
        if (in_array($url, $favorites)) {
            // Output error message if the URL already exists
            echo 'This URL has already been saved.';
        } else {
            // Open in write mode and curl the file
            $handle = fopen($file, 'a');
            if (flock($handle, LOCK_EX)) {
                // Write URL to the text file
                fwrite($handle, $url . PHP_EOL);

                // Output confirmation message
                echo 'URL was saved: ' . $url;

                // Release the file and close the handle
                flock($handle, LOCK_UN);
                fclose($handle);
            } else {
                // Output error message if file curling failed
                echo 'The file curling has failed.';
            }

            // Releasing the lock file and closing the handle
            flock($lockHandle, LOCK_UN);
            fclose($lockHandle);
        }
    } else {
        // Output error message if the URL is invalid
        echo 'Invalid URL';
    }

    // Check if maximum number of requests per minute has been exceeded
    $max_requests_per_minute = 5;
    if (isset($_SESSION['last_request_time'])) {
        $elapsed_time = time() - $_SESSION['last_request_time'];
        $requests_per_minute = $_SESSION['requests_per_minute'] + 1;
        if ($elapsed_time >= 60) {
            $requests_per_minute = 1;
        }
        if ($requests_per_minute > $max_requests_per_minute) {
          header('HTTP/1.1 429 Too Many Requests');
          header('Retry-After: 60');
          die('Too many requests. Please wait a minute.');
        }
    } else {
      $requests_per_minute = 1;
    }
    $_SESSION['last_request_time'] = time();
    $_SESSION['requests_per_minute'] = $requests_per_minute;
    exit; // Exit the script to prevent the form from being displayed
}

// Read all saved URLs from text file
$favorites = file($file, FILE_IGNORE_NEW_LINES);
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Simple Web-Link-Tracker</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'">
    <meta http-equiv="X-Frame-Options" content="SAMEORIGIN">
</head>
<body>
  <!-- List of all saved URLs -->
  <ul>
    <?php foreach ($favorites as $favorite) { ?>
      <li><a href="<?php echo $favorite; ?>" rel="noopener noreferrer"><?php echo $favorite; ?></a></li>
    <?php } ?>
  </ul>
</body>
</html>
