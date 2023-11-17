import socket
import threading
from tictactoe import TicTacToe

# Global variables
host = socket.gethostbyname(socket.gethostname()) # Get the host name
port = 55555


def handle_client (client, player, game):
    client.send(str.encode('Welcome to Tic Tac Toe!'))

    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if data == 'QUIT': # If the client wants to quit
                break
            elif data == 'RESTART': # If the client wants to restart
                game.restart()
            elif data == 'SHOW': # If the client wants score board
                game.show()
            elif data == 'HELP': # If the client wants help navigating
                game.help()
            elif data == 'PLAY': # If the client wants to start the game
                game.play(player)
            else:
                client.send(str.encode('Invalid input!'))
        
            if player == game.player and data.startswith('MOVE'):
                move_str, move_value = data.split(' ')
                if move_str == 'MOVE':
                    move = int(move_value)
                    if game.validMove(move, player):
                        game.makeMove(move, player)
                        game.show()
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
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the IPv4, SOCK_STREAM is TCP 
    server.bind((host, port))                                # Bind the server to the host and port
    server.listen(2)                                        # Listen for 2 connections

    print(f"Server is listening on {host}:{port}")         # Print the server is listening
    game = TicTacToe()                                           # Create the game
    game.restart()  
    game.show() 
    while True:
        client, address = server.accept()                  # Accept a connection
        print(f"Connected has been established with {address}") 
           
        player = game.go2OthPlayer()                   # Get the player
        game.addPlayer(player)                            # Add the player to the game

        thread = threading.Thread(target=handle_client, args=(client, player, game)) # Create a thread for the client
        thread.start()                              # Start the thread

if __name__ == '__main__':
    start()