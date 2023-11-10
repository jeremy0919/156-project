import socket


HEADER = 64 #header is the same
PORT = 60061 #ports have to match
SERVER = "localhost" #"192.168.56.1"  #client server is this
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(ADDR)
client.connect((SERVER, 60060))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)