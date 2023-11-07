<!DOCTYPE html>
<html5>
    <head>
        <link rel="stylesheet" href="style1.css">
        <script src="script.js">
        </script>
    </head>

    <body>
        <form>
            <input type = "button" onclick="createTable()" value = "click me">
        </form>
      

        <div class = "new"></div>

        <table class = "scoreTab">
            <head>
                <tr>
                    <td>
                        Player
                    </td>
                    <td>
                        score
                    </td>
                </tr>
            </head>
            <tbody>
                <tr>
                    <td>
                        Player 1
                    </td>
                    <td id = "score1"> 0 </td>
                </tr>
                <tr>
                <td>
                    Player 2
                </td>
                <td id = "score2"> 0</td>
            </tr>
            </tbody>
        </table>

        <table class ="table2">
            <tbody>
                <tr>
                    <td> player name:</td>
                    <td id ="playerName"></td>
                </tr>
                <tr>
                    <td>gamesPlayed</td>
                    <td id ="gamesPlayed"></td>
                </tr>
                <tr>
                    <td>wins</td>
                    <td id = "wins1" ></td>
                </tr>
                <tr>
                    <td>losses</td>
                    <td id ="losses1"></td>
                </tr>
                <tr>
                    <td>winRate</td>
                    <td id ="winRate1"></td>
                </tr>
            <tbody>

        </table>
        <div class = "table" ></div>
    </body>
</html5>