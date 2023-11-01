<?php // start at log in page, log in page goes to selection of one or two player
// Read the existing JSON file
if(isset($_POST['submit'])){
$json_file = 'database.json';
$json_data = file_get_contents($json_file);
$users = json_decode($json_data, true);
foreach($users as $key =>$value){
    echo"{$key} = {$value} <br>";
}
}
// Get data from the form


// Encode the updated data back to JSON
//$updated_json = json_encode($users, JSON_PRETTY_PRINT);

// Write the updated JSON data back to the file
//file_put_contents($json_file, $updated_json);


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form action="login.php" method="post">
        <label>login:</label>
        <input type="text" name="username"> <br>
        <input type="submit" name="submit" value="login"><br>
</body>
</html>