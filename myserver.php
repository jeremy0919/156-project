<?php
//use global variable from video to pass data along\
//could always remove this file and add buttons dynamically after log in
if (isset($_POST['submit'])) {
    header('Location: tic-tac-toe.php');
}
if (isset($_POST['submit1'])) {
    header('Location: tic-tac-toe2.php');
}


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form action="myserver.php" method="post">

        <input type="submit" name="submit" value="singlePlayer"><br>
</body>

<form action="myserver.php" method="post">
        
        <input type="submit" name="submit1" value="Multiplayer"><br>
</body>
</body>
</html>