import socket
import threading
import tkinter as tk
from tkinter import messagebox

host = socket.gethostbyname(socket.gethostname())  # Get the host name
playerNum = int(input('Enter player tag (1 or 2)'))  # Get the player number


class TicTacToeGUI(tk.Tk):
    def __init__(self, client_socket, player_num):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x300")

        self.client_socket = client_socket
        self.player_symbol = 'X' if player_num == 1 else 'O'
        self.game_over = False

        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            button = tk.Button(self, text='', width=10, height=3, command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)

        self.menu_frame = tk.Frame(self)
        self.menu_frame.grid(row=3, column=0, columnspan=3)

        restart_button = tk.Button(self.menu_frame, text="Restart", command=self.restart_game)
        restart_button.grid(row=0, column=0)

        show_button = tk.Button(self.menu_frame, text="Show Board", command=self.show_board)
        show_button.grid(row=0, column=1)

        help_button = tk.Button(self.menu_frame, text="Help", command=self.help_navigation)
        help_button.grid(row=0, column=2)

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def make_move(self, index):
        # Check if the game is over or the button is already clicked
        if self.game_over or self.buttons[index]["text"] != "":
            return

        # Update the button text with the player's symbol
        self.buttons[index]["text"] = self.player_symbol

        # Send the move to the other player through the network
        move_message = f"MOVE {index} {self.player_symbol}"
        self.client_socket.send(move_message.encode())

    def restart_game(self):
        data = 'RESTART'
        self.client_socket.send(str.encode(data))

    def show_board(self):
        data = 'SHOW'
        self.client_socket.send(str.encode(data))

    def help_navigation(self):
        data = 'HELP'
        self.client_socket.send(str.encode(data))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                print(message)

                if message == 'You won!' or message == 'You tied!':
                    self.game_over = True
                    break
                elif message.startswith('MOVE'):
                    _, move_value = message.split(' ')
                    move = int(move_value) - 1  # Subtracting 1 to convert to 0-indexed for GUI
                    self.update_board(move)
                    self.make_move(self,move,self.player_symbol)
                elif message == 'Invalid move!':
                    messagebox.showinfo("Invalid Move", "Please make a valid move.")
                elif message == "Not your turn!":
                    messagebox.showinfo("Not Your Turn", "It's not your turn.")
            except ConnectionResetError:
                break

    def update_board(self, move):
        if 0 <= move < 9 and self.buttons[move]['text'] == '':
            self.buttons[move].config(text=self.player_symbol, state=tk.DISABLED)
        else:
            print("Invalid move received from the server.")


if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, 55555))

    print(f"You are player {playerNum}\n")

    gui = TicTacToeGUI(client_socket, playerNum)
    gui.mainloop()

    client_socket.send(str.encode('QUIT'))
    client_socket.close()