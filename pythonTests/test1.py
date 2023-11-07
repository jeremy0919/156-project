#gpt code start

import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_socket.bind(('0.0.0.0', 12345))

# Listen for incoming connections
server_socket.listen(2)
print("Waiting for players to connect...")

# Accept two client connections
player1_socket, player1_address = server_socket.accept()
print(f"Player 1 connected from {player1_address}")
player2_socket, player2_address = server_socket.accept()
print(f"Player 2 connected from {player2_address}")

#gpt code end

#game logic

