import socket
import threading
from tictactoe import TicTacToe

# Global variables
host = socket.gethostbyname(socket.gethostname())
port = 55555


def handle_client(client, player, game):
    client.send(str.encode('Welcome to Tic Tac Toe!'))

    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if data == 'QUIT':
                break
            elif data == 'RESTART':
                game.restart()
            elif data == 'SHOW':
                game.show()
            elif data == 'HELP':
                game.help()
            elif data == 'PLAY':
                game.play(player)
            else:
                client.send(str.encode('Invalid input!'))

            if player == game.player and data.startswith('MOVE'):
                move_str, move_value = data.split(' ')
                if move_str == 'MOVE':
                    move = int(move_value)
                    if game.validMove(move, player):
                        game.makeMove(move, player)
                        game.show_updated_board() 
                        if game.isWinner(player):
                            client.send(str.encode('You won!'))
                            break
                        elif game.isBoardFull():
                            client.send(str.encode('You tied!'))
                            break
                        else:
                            game.go2OthPlayer()
                    else:
                        client.send("Invalid move!".encode('utf-8'))
                else:
                    client.send("Not your turn!".encode('utf-8'))
        except ValueError:
            client.send("Pick a number between 1 and 9!".encode('utf-8'))

    print(f"Lost connection with {player}")
    client.close()


def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(2)

    print(f"Server is listening on {host}:{port}")
    game = TicTacToe()
    game.restart()
    game.show_updated_board() 

    while True:
        client, address = server.accept()
        print(f"Connected has been established with {address}")

        player = game.go2OthPlayer()
        game.addPlayer(player)
        thread = threading.Thread(target=handle_client, args=(client, player, game))
        thread.start()


if __name__ == '__main__':
    start()