import socket
import threading
import time
import random

host = socket.gethostbyname(socket.gethostname()) #comment out if not using same computer to host and play
#show how many people are in the room and connect with them
"""
while(True):
    room_number = int(input("Enter the room number you want to join: "))

    Gamemode = input("S for Single player or M for multiPlayer \n")
    if(Gamemode == "S"):
       # print("do something")
        playerNum = 1 #auto sets playernum to one so playernum 2 can be hardcoded as computer
        break
    if(Gamemode=="M"):
        playerNum = int(input('Enter player tag (1 or 2)'))
        break
  #  if(Gamemode=="C"):
   #     playerNum = 1
   #     break
"""
def rec_message(client_socket):
    while True:
        message = client_socket.recv(2048).decode('utf-8')
        if message:
            if not message.endswith(str(playerNum)) and not message.endswith("CPU"):
                print(message)

        if message.startswith('You won!') or message.startswith('You tied!')or message.startswith('CPU won!'):
            print("type restart to restart or quit to exit")
        if(message.startswith('Game is restarting!')):
            print("Make your move: \n")
        if(message.startswith('pick your room number 1-5')):
           print('\n')
           NewMessage = input()
           client_socket.send(str.encode(NewMessage))
        while(message.endswith('CPU')): # in theory when it recieves a message back that ends in cpu
            loc = random.randint(1, 9) # keeps sending messages for random moves
            message = f'SMOVE {loc} Made by player {0}' #on behalf of player 0/CPU to server
            client_socket.send(str.encode(message))



def inGame1(client_socket):
    time.sleep(.2) #neccisary if using input text but print statements often overlap input text
    while True:
        print("ingame1 ")
        try:
            data = f'SHOW SMOVE'
            client_socket.send(str.encode(data)) #by using this each time might not need cpu move
            
            temp = input()                      #takes in input from client side
            move = None                         #declaration
            print(f'input is {temp}\n')
            try:
                move = int(temp)                #converts input to an int
            except ValueError:
                pass

            if temp.upper() in ["HELP", "RESTART", "SHOW", "QUIT"]:  #for some reason upper() does not work
                data = f'{temp} SMOVE'
                print(f'data is {data}\n')
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
    print("ingame")
    while True:
        try:
        #    data = f'SHOW'
        #    client_socket.send(str.encode(data)) #by using this each time might not need cpu move
            
         
            temp = input()          
            move = None
            print(f'input is {temp}\n')
            try:
                move = int(temp)
            except ValueError:
                pass

            if temp.upper() in ["HELP", "RESTART", "SHOW", "QUIT"]:  #for some reason upper() does not work
                data = f'{temp}'
                print(f'data is {data}\n')
                client_socket.send(str.encode(data))
                break
            elif move is not None and 1 <= move <= 9:
                data = f'MOVE {move} Made by player {playerNum}'  #sends data to server, important pieces are MOVE, move, playerNum
                print(f'data is {data}\n')
                client_socket.send(str.encode(data))
                break
            else:
                print('Invalid move! \n')
                continue

        except ValueError:
            print('Invalid move! Please enter a number between 1 and 9')
            continue


def connect_to_server(host, port, playerNum, Gamemode, room_number):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    if playerNum == 1:
        playerNum = 1
        print("")
    else:
        playerNum = 0
    
    if Gamemode != "C":
        print(f"You are player {playerNum} in room {room_number}\n")
        if Gamemode == "M":
            print("Second Player to enter goes first (Be polite ;p)")
    
    time.sleep(1)  # Add a small delay before sending the 'HELLO' message
    client_socket.send(str.encode(f'HELLO Player {playerNum} in room {room_number}'))

    thread = threading.Thread(target=rec_message, args=(client_socket,))
    thread.start()

    while True:
        if Gamemode == "S":
            inGame1(client_socket)
        elif Gamemode == "M":
            inGame(client_socket)
        # Add more conditions for other game modes if needed

if __name__ == "__main__":
   # host = "10.62.77.88"
    port = 55555
    #playerNum = 0
  #  Gamemode = "M"
    room_number = int(input("Enter the room number you want to join: "))

    Gamemode = input("S for Single player or M for multiPlayer \n")
    if(Gamemode == "S"):
       # print("do something")
        playerNum = 1 #auto sets playernum to one so playernum 2 can be hardcoded as computer
  
    if(Gamemode=="M"):
        playerNum = int(input('Enter player tag (1 or 2)'))
    # Prompt the player to choose a room number

    connect_to_server(host, port, playerNum, Gamemode, room_number)
