import socket
import threading
from tictactoe import TicTacToe


host = socket.gethostbyname(socket.gethostname())
port = 55555

def handle_client(client, player, game, clients_lock):
    client.send(str.encode('Tic Tac Toe!'))

    while True:
        try:
            data = client.recv(1024).decode('utf-8')


            if data.startswith('QUIT'):                                                  # If the client wants to quit
                break
            elif data.startswith('RESTART'):                                             # If the client wants to restart
                game.restart()
            elif data.startswith('SHOW'):                                                # If the client wants score board
                client.send(str.encode(game.show2())) #idk if this will work
            elif data.startswith('HELP'):                                                # If the client wants help navigating
                client.send(str.encode(game.help()))
            elif data.startswith('PLAY'):                                                # If the client wants to start the game
                game.play(player)
            else:
                message = f'Your turn is over.\n'
                client.send(str.encode(message))
            if player == game.player and data.startswith('MOVE'):              # If it is the player's turn
                move_str, move_value, a,b,c,PrevPlayer = data.split(' ')                  # splits data being recieved into string and the value
                if move_str == 'MOVE':                                         # If the client wants to make a move
                    move = int(move_value)                                     # sets var move to move int from data
                    if game.validMove(move, player):                           # checks if move is valid
                        game.makeMove(move, player)                            # if valud makes move
                        game.show()                                            # prints the board in the console with the move
                        if game.isWinner(player):
                            message = game.show2()
                            client.send(str.encode(f'You won! \n {message}'))
                            break
                        elif game.isBoardFull():
                            message = game.show2()
                            client.send(str.encode(f'You tied! \n {message}'))
                            break
                        else:
                            game.go2OthPlayer()   
                            with clients_lock:                                                          #not entirely sure
                                for other_client in clients:                                            # broadcasts to all clients
                                    print(other_client)
                                    try:
                                        other_client.send(str.encode(data))                             # whats sent on one client dispalys on the other
                                    except:
                                        # Handle potential disconnection
                                        pass
                                                        #if game is not over tells client its the other players move
                    else:
                        client.send("Invalid move!\n".encode('utf-8'))        
                else:
                    client.send("Not your turn!\n".encode('utf-8'))
  
        except ValueError:
            client.send("Pick a number between 1 and 9!\n".encode('utf-8'))

    client.close()
    print(f"Lost connection with {player}")
    with clients_lock:
        clients.remove(client)
    client.close()

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(2)

    print(f"Server is listening on {host}:{port}")

    game = TicTacToe()
    game.restart()  
    game.show() 
    #Chat gpt
    clients_lock = threading.Lock()
    global clients #makes client list so moves can be sent to all clients
    clients = []

    while True:
        client, address = server.accept()
        print(f"Connected has been established with {address}")

        with clients_lock:
            clients.append(client)
#end chatGPT
        player = game.go2OthPlayer()
        game.addPlayer(player)

        thread = threading.Thread(target=handle_client, args=(client, player, game, clients_lock))
        thread.start()

if __name__ == '__main__':
    start()