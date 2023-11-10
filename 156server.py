import socket
import threading
import time


HEADER = 64
PORT = 60060 #ports over 4000 (sike, my ports are up to 6k) are typically inactive or unused
#SERVER = '192.168.1.22"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

try:   
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
except socket.error as e:
    print(f"Error creating/connecting socket: {e}")
    exit(1)
    
def handle_client(conn, addr):
    print("[NEW CONNECTION]{addr} connected.") 

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int (msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


print("[STARTING] server is starting")
start()