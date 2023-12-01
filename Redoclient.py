import socket
import threading
import time

#host = socket.gethostbyname(socket.gethostname())
playerNum = int(input('Enter player tag (1 or 2)'))

def rec_message(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            if not message.endswith(str(playerNum)):
                print(message)
         #   if message.startswith('Tic Tac Toe!'): # too much time trying to get to print right 
              #  print("Move:", end="")  # Print "Move:" only when it's the current player's turn
        if message.startswith('You won!') or message.startswith('You tied!'):
          #  print(message)
            break

def inGame(client_socket):
    time.sleep(.2)
    while True:
        try:
         
            temp = input()          
            move = None

            try:
                move = int(temp)
            except ValueError:
                pass

            if temp.upper() in ["HELP", "RESTART", "SHOW", "QUIT"]:
                data = f'{temp}'
                client_socket.send(str.encode(data))
                break
            elif move is not None and 1 <= move <= 9:
                data = f'MOVE {move} Made by player {playerNum}'
                client_socket.send(str.encode(data))
                break
            else:
                print('Invalid move! \n')
                continue

        except ValueError:
            print('Invalid move! Please enter a number between 1 and 9')
            continue

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.1.171"
    client_socket.connect((host, 55555))

    if playerNum == 1:
        playerNum = 1
        print("")
    else:
        playerNum = 2

    print(f"You are player {playerNum}\n")
    print("Second Player to enter goes first (Be polite ;p)")

    thread = threading.Thread(target=rec_message, args=(client_socket,))
    thread.start()

    while True:
        inGame(client_socket)