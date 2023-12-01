import socket
import threading
from tictactoe import TicTacToe

# Global variables
host = socket.gethostbyname(socket.gethostname())                               # Get the host name
port = 55555

def handle_client (client, player, game):
    client.send(str.encode('Tic Tac Toe!'))

    while True:
        try:
            data = client.recv(1024).decode('utf-8')                            #recieves data sent over connection, max of 1024 bytes of data, decodes using utf-8 to convert into unicode string
            
            if data.startswith('QUIT'):                                                  # If the client wants to quit
                break
            elif data.startswith('RESTART'):                                             # If the client wants to restart
                game.restart()
            elif data.startswith('SHOW'):                                                # If the client wants score board
                client.send(str.encode(game.show())) #idk if this will work
            elif data.startswith('HELP'):                                                # If the client wants help navigating
                game.help()
            elif data.startswith('PLAY'):                                                # If the client wants to start the game
                game.play(player)
            else: # need to put this somewhere else so it cant send this string, you won/invalid move in the same turn
                client.send(str.encode('Your turn is over. \n Its player {player}s turn now!'))
        
            if player == game.player and data.startswith('MOVE'):              # If it is the player's turn
                move_str, move_value = data.split(' ')                  # splits data being recieved into string and the value
                if move_str == 'MOVE':                                         # If the client wants to make a move
                    move = int(move_value)                                     # sets var move to move int from data
                    if game.validMove(move, player):                           # checks if move is valid
                        game.makeMove(move, player)                            # if valud makes move
                        game.show()                                            # prints the board in the console with the move
                        if game.isWinner(player):
                            client.send(str.encode('You won!'))
                            break
                        elif game.isBoardFull():
                            client.send(str.encode('You tied!'))
                            break
                        else:
                            game.go2OthPlayer()                                #if game is not over tells client its the other players move
                    else:
                        client.send("Invalid move!".encode('utf-8'))        
                else:
                    client.send("Not your turn!".encode('utf-8'))
        except ValueError:
             client.send("Pick a number between 1 and 9!".encode('utf-8'))     #conditional for if data recieved isnt an int of 1-9

    client.close()
    print(f"Lost connection with {player}")
    client.close()

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                      # AF_INET is the IPv4, SOCK_STREAM is TCP 
    server.bind((host, port))                                                       # Bind the server to the host and port
    server.listen(2)                                                                # Listen for 2 connections

    print(f"Server is listening on {host}:{port}")                                  # Print the server is listening
    game = TicTacToe()                                                              # Create the game
    game.restart()  
    game.show() 
    while True:
        client, address = server.accept()                                           # Accept a connection
        print(f"Connected has been established with {address}") 
           
        player = game.go2OthPlayer()                                                # Get the player
        game.addPlayer(player)                                                      # Add the player to the game

        thread = threading.Thread(target=handle_client, args=(client, player, game)) # Create a thread for the client
        thread.start()                                                              # Start the thread

if __name__ == '__main__':
    start()
