<?php // start at log in page, log in page goes to selection of one or two player // start at log in page, log in page goes to selection of one or two player
// Read the existing JSON file

if (isset($_POST['submit'])) {
    $json_file = 'database.json';
    $json_data = file_get_contents($json_file);
    $data = json_decode($json_data, true);

    $name = trim($_POST['username']);
    $check = 0;
    if (isset($data['User']) && is_array($data['User'])) {
        foreach ($data['User'] as $key => $user) {
            if ($user['name'] == $name) {
                echo "{$key} = {$user['name']} <br>";
                echo "{$key} = {$user['gamesPlayed']} <br>";
                echo "{$key} = {$user['wins']} <br>";
                echo "{$key} = {$user['losses']} <br>";
                echo "{$key} = {$user['winRate']} <br>";
                $check = 1;
            }
        }
    }

    echo $name;
if($check=0){
$new_username = [
    
    "name"=>$name,
    "gamesPlayed"=>0,
    "wins"=> 0,
    "losses"=>0,
    "winRate"=> 0
];
$data['User'][] = $new_username;

// Encode the updated data back to JSON
$updated_json = json_encode($data, JSON_PRETTY_PRINT);

// Write the updated JSON data back to the file
file_put_contents($json_file, $updated_json);
}
header('Location: myserver.php');
}
// Get data from the form

//header('Location: lab8.php');

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
<body style="background-image: url('wp7601179-retro-80s-arcade-wallpapers.jpg')">
<form action="login.php" method="post">
        <label style = "color:white">login:</label>
        <input type="text" name="username"> <br>
        <input type="submit" name="submit" value="login"><br>
</body>
</html>