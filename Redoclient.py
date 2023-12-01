import socket
import threading


host = socket.gethostbyname(socket.gethostname()) # Get the host name
playerNum = int(input('Enter player tag (1 or 2)')) # Get the player number
def rec_message(client_socket):
    while True:                                         
        message = client_socket.recv(1024).decode('utf-8') # Receive the message
        print(message)                                     # Print the message
        if message == 'You won!' or message == 'You tied!': # If the game is over
            break
        else:
            continue

def inGame(client_socket):
    while True:
        try:
            temp = (input('Move: '))                 #prints move and waits for input
            move = int(temp)
            if(temp == "HELP" or temp == "RESTART" or temp == "SHOW" or temp =="QUIT"):
                data = f'{temp}'
                client_socket.send(str.encode(data))
                break
            elif move < 1 or move > 9: #doesnt allow us to use any server functions, ie help show restart, need to either remove those or change this
                print('Invalid move! \n')                  #if move is invalid do nothing
                continue
            
            else:
                data = f'MOVE {move}'                   #if move is valid ties MOVE with input so server knows its a move command
                #print(f'Sending data: {data}')
                client_socket.send(str.encode(data))
                break
        except ValueError:
            print('Invalid move! Please enter a number between 0 and 9')
            continue

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the IPv4, SOCK_STREAM is TCP
    client_socket.connect(( host, 55555))                                 # Connect to the server

               # Receive the player number
    if playerNum == 1:                                                  # If the player is 1
        playerNum = 1                                                   # Set the player number to 2
        print("")
    else:                                                               # Else
        playerNum = 2             
    print(f"You are player {playerNum}\n")                              # Print the player number
    print("Second Player to enter goes first (Be polite ;p)")

    thread = threading.Thread(target=rec_message, args=(client_socket,)) # Create a thread for the client
    thread.start()                                                     # Start the thread

    while True:
        inGame(client_socket)                                          # Play the game
