import socket
import threading
from tictactoe import TicTacToe
import time

host = socket.gethostbyname(socket.gethostname())
port = 55555

def handle_client(client, player, game, clients_lock):
    client.send(str.encode('Tic Tac Toe!'))

    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            print(f"data after send {data}")
            print(f"Player is  {game.player}")
            print(f"current player is  {[player]}")
            if(player == 2):
                player =1
                game.player =1
            if data.startswith('QUIT SMOVE'):                                                  # If the client wants to quit
                for other_client in clients:                                            # broadcasts to all clients  
                    try:
                        client.send(str.encode("QUITTING")) 
                    except:
                        pass
                break
            elif data.startswith('QUIT'):                                                  # If the client wants to quit
                for other_client in clients:                                            # broadcasts to all clients  
                    try:
                        client.send(str.encode("QUITTING")) 
                    except:
                        pass
                break
            elif data.startswith('RESTART SMOVE'):                                             # If the client wants to restart
                client.send(str.encode("game is restarting")) 
                game.restart()
         
                
            elif data.startswith('RESTART'):                                             # If the client wants to restart
                game.restart()
                for other_client in clients:                                            # broadcasts to all clients  
                    try:
                        client.send(str.encode("game is restarting")) 
                    except:
                        pass
            elif data.startswith('SHOW SMOVE'):                                                # If the client wants score board
                client.send(str.encode(game.show2())) #sends to only one client
            elif data.startswith('HELP SMOVE'):                                                # If the client wants help navigating
                client.send(str.encode(game.help()))
            elif data.startswith('PLAY SMOVE'):                                                # If the client wants to start the game
                game.play(player)
            elif data.startswith('SHOW'):                                                # If the client wants score board
                client.send(str.encode(game.show2())) #sends to only one client
            elif data.startswith('HELP'):                                                # If the client wants help navigating
                client.send(str.encode(game.help()))
            elif data.startswith('PLAY'):                                                # If the client wants to start the game
                game.play(player)
            
            elif(data.endswith("player 0")):
                player =0
            elif(data.endswith("player 1")) and data.startswith("SMOVE"):
                player = 1
                message = f'Your turn is over.\n'
                client.send(str.encode(message))
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
                            for other_client in clients:                                            # broadcasts to all clients
                                  #  print(other_client)
                                    try:
                                        other_client.send(str.encode(message))                             # whats sent on one client dispalys on the other
                                    except:
                                        # Handle potential disconnection
                                        pass
                            client.send(str.encode(f'You won! \n'))
                       #     break
                        elif game.isBoardFull():
                            message = game.show2()
                            for other_client in clients:                                            # broadcasts to all clients
                                 #   print(other_client)
                                    try:
                                        other_client.send(str.encode(message))                             # whats sent on one client dispalys on the other
                                    except:
                                        # Handle potential disconnection
                                        pass
                            client.send(str.encode(f'You tied! \n'))
                         #   break
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
            elif player == game.player and data.startswith('SMOVE'):              # If it is the player's turn
                condCheck = 0
              #  print(f"data in elif {data}")
                move_str, move_value, a,b,c,PrevPlayer = data.split(' ')                  # splits data being recieved into string and the value
                if move_str == 'SMOVE':                                         # If the client wants to make a move
                    move = int(move_value)
                    if game.isBoardFull():
                            message = game.show2()
                            client.send(str.encode(f'You tied! \n'))
                            PrevPlayer = 2
                            condCheck = 2                                     # sets var move to move int from data
                            player = 2
                    elif game.validMove(move, player):                           # checks if move is valid
                        condCheck = 1
              #          print("passing into valid move\n")
                        game.makeMove(move, player)                            # if valud makes move
                        game.show()                                            # prints the board in the console with the move
                        if game.isWinner(player):
                            message = game.show2()
                            client.send(str.encode(f'You won! \n'))
                            PrevPlayer = 2
                            player = 2
                            condCheck = 2
                            #break
                        elif game.isBoardFull():
                            message = game.show2()
                            client.send(str.encode(f'You tied! \n'))
                            PrevPlayer = 2
                            condCheck = 2
                           # break
                        else:
                            game.go2OthPlayer()
                            if( game.player ==0 and player == 1):
                                client.send(str.encode(f'SMOVE CPU' )) #should encode SMOVE and other cpu player
                            elif (player == 0   ):       
                                message = f'Move made at {move_value}, CPU turn over'
                                player =1
                                client.send(str.encode(message)) 
                #    print(f"condCheck is: {condCheck}, and previous player is: {PrevPlayer} for the data: {data}\n which is sending {move} and {player} into valud move \n")
                    if(int(PrevPlayer)  and (int(condCheck) ==0)): #hard codes in player 1 invalid move
                        client.send("Invalid move!\n".encode('utf-8'))
                    if((int(PrevPlayer) == 0) and (int(condCheck) == 0)): #should loop cpu if not valid move 
             #           print("SMOVE loop") 
                        client.send(str.encode(f'SMOVE CPU' )) 
                 
                    
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