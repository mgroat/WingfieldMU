<html>
<body bgcolor="black" onload="javascript:window.self.location.href='#bot'">
<font color="white" size="1">

<?
  if (strlen($_POST["data"]) > 0 ) { 
    $data = $_POST["data"] . "\n";
    $fp = fsockopen("localhost", 4077, $errno, $errstr, 30);
    fwrite($fp,$data);
    fclose($fp);
    sleep(1); #Otherwise, we don't see the result of our command
  }
  print `tail -n 50 log.log`; #This is incompatable with Windows servers.
?>

<form action="output.php" method="post">
<input type="text" name="data"><br>
<input type="submit">

<a name="bot"></a>

</body>
<html>
