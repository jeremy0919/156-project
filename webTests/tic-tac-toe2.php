<!DOCTYPE html>
<html5>
    <head>
        <link rel="stylesheet" href="style.css">
        <script src="script2.js">
        </script>
    </head>

    <body>
        <form>
            <input type = "button" onclick="createTable()" value = "click me">
        </form>
        <div class = "table"></div>

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
    </body>
</html5>