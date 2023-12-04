import socket
import threading
import time
import random

host = socket.gethostbyname(socket.gethostname()) #comment out if not using same computer to host and play
while(True):
    Gamemode = input("S for Single player or M for multiPlayer \n")
    if(Gamemode == "S"):
       # print("do something")
        playerNum = 1; #auto sets playernum to one so playernum 2 can be hardcoded as computer
        break
    if(Gamemode=="M"):
        playerNum = int(input('Enter player tag (1 or 2)'))
        break

def rec_message(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            if not message.endswith(str(playerNum)) and not message.endswith("CPU"):
                print(message)

        if message.startswith('You won!') or message.startswith('You tied!')or message.startswith('CPU won!'):
            print("type restart to restart or quit to exit")
        if(message.startswith('Game is restarting!')):
            print("Make your move: \n")
      
        while(message.endswith('CPU')): # in theory when it recieves a message back that ends in cpu
            loc = random.randint(1, 9) # keeps sending messages for random moves
            message = f'SMOVE {loc} Made by player {0}' #on behalf of player 0/CPU to server
            client_socket.send(str.encode(message))



def inGame1(client_socket):
    time.sleep(.2) #neccisary if using input text but print statements often overlap input text
    while True:
        try:
            data = f'SHOW SMOVE'
            client_socket.send(str.encode(data)) #by using this each time might not need cpu move
            
            temp = input()                      #takes in input from client side
            move = None                         #declaration

            try:
                move = int(temp)                #converts input to an int
            except ValueError:
                pass

            if temp.upper() in ["HELP", "RESTART", "SHOW", "QUIT"]:  #for some reason upper() does not work
                data = f'{temp} SMOVE'
                client_socket.send(str.encode(data))                #sends non move commands
                break
            elif move is not None and 1 <= move <= 9:
                data = f'SMOVE {move} Made by player {playerNum}'   #sends data to server, important pieces are SMOVE, move, playerNum
                client_socket.send(str.encode(data))                #extra words exists for easy debugging ^
                break
            else:
                print('Invalid move! \n')                           #prints invalid move and stays in loop
                continue

        except ValueError:
            print('Invalid move! Please enter a number between 1 and 9')
            continue

def inGame(client_socket):
    time.sleep(.2) #neccisary if using input text but print statements often overlap input text
 
    while True:
        try:
        #    data = f'SHOW'
        #    client_socket.send(str.encode(data)) #by using this each time might not need cpu move
            
         
            temp = input()          
            move = None

            try:
                move = int(temp)
            except ValueError:
                pass

            if temp.upper() in ["HELP", "RESTART", "SHOW", "QUIT"]:  #for some reason upper() does not work
                data = f'{temp}'
                client_socket.send(str.encode(data))
                break
            elif move is not None and 1 <= move <= 9:
                data = f'MOVE {move} Made by player {playerNum}'  #sends data to server, important pieces are MOVE, move, playerNum
                client_socket.send(str.encode(data))
                break
            else:
                print('Invalid move! \n')
                continue

        except ValueError:
            print('Invalid move! Please enter a number between 1 and 9')
            continue

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #start server, get ip printed on screen declare host to it on line below
    #host = "192.168.1.171" #modify based off of host server IP
    client_socket.connect((host, 55555))                               #ensure port is open

    if playerNum == 1:
        playerNum = 1
        print("")
    else:
        playerNum = 0

    print(f"You are player {playerNum}\n")
    if(Gamemode == "M"):
        print("Second Player to enter goes first (Be polite ;p)")

    thread = threading.Thread(target=rec_message, args=(client_socket,))
    thread.start()

    while True:
        if(Gamemode == "S"):                    #if game mode is single player 
            inGame1(client_socket)
        if(Gamemode == "M"):                    #if game mode is multiplayer
            inGame(client_socket)