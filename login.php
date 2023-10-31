<?php
// Read the existing JSON file
$json_file = 'database.json';
$json_data = file_get_contents($json_file);
$users = json_decode($json_data, true);

// Get data from the form
if(isset($_POST['submit'])){
    if($_POST['username'] != null){

    $pokemon = $_POST['Pokemon'] ;
}

if($_POST['canEvolve'] != null && $_POST['weakTo'] != null&& $_POST['type'] != null&& $_POST['averageSize'] != null&& $_POST['shinyColor'] != null&& $_POST['evolution'] != null && $_POST['Pokemon'] != null){
$new_pokemon = [
    
    'name' => $pokemon ,
    'evolution' => $evolution,
    'shinyColor' =>    $shinyColor ,
    'averageSize' =>  $averageSize ,
    'type' =>   $type,
    'weakTo' =>  $weakTo ,
    'canEvolve' =>  $canEvolve,
    'img' =>   $img,
];
$users['user'][] = $user;

// Encode the updated data back to JSON
$updated_json = json_encode($users, JSON_PRETTY_PRINT);

// Write the updated JSON data back to the file
file_put_contents($json_file, $updated_json);
}
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
<form action="login.php" method="post">
        <label>login:</label>
        <input type="text" name="username"> <br>
        <input type="submit" name="submit" value="login"><br>
</body>
</html>