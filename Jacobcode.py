from tkinter import *

root = Tk()
root.title("TicTacToe Game")
player = 'X'

def winner(player): # X = 1 || O = 2 || N = Tie
    # Disable Buttons
    my_button11.config(state='disabled')
    my_button12.config(state='disabled')
    my_button13.config(state='disabled')
    my_button21.config(state='disabled')
    my_button22.config(state='disabled')
    my_button23.config(state='disabled')
    my_button31.config(state='disabled')
    my_button32.config(state='disabled')
    my_button33.config(state='disabled')
    for client in clients:
        try:
            client.send(f"Winner:{player}".encode())
        except socket.error as e:
            print(f"Error sending data to client: {e}")

    if player == 'N': player_statement = "Tie Game"
    elif player == 'X': player_statement = "Player 1 Wins"
    else: player_statement = "Player 2 Wins"
    # Print Label - Global Since needed in New Game
    global winner_label 
    winner_label = Label(text=player_statement, font =('ariel', 22))
    winner_label.grid(row = 1, column = 1, rowspan = 3, columnspan = 3)

def checkFull():
    # Return False if at least one is empty
    if my_button11['text'] == '': return False
    elif my_button12['text'] == '': return False
    elif my_button13['text'] == '': return False
    elif my_button21['text'] == '': return False
    elif my_button22['text'] == '': return False
    elif my_button23['text'] == '': return False
    elif my_button31['text'] == '': return False
    elif my_button32['text'] == '': return False
    elif my_button33['text'] == '': return False
    return True

def chosen():
    # Move To Next Player
    global player
    if player =='X': player = 'O'
    else: player = 'X'
    # If Board Full, Winner func w/ Tie
    if checkFull(): winner('N')

def winCond():
    # Check Horizontal
    if my_button11['text'] == my_button12['text'] == my_button13['text'] and my_button11['text'] != '': return True
    elif my_button21['text'] == my_button22['text'] == my_button23['text'] and my_button21['text'] != '': return True
    elif my_button31['text'] == my_button32['text'] == my_button33['text'] and my_button31['text'] != '': return True
    # Check Diagonal
    if my_button11['text'] == my_button22['text'] == my_button33['text'] and my_button11['text'] != '': return True
    elif my_button13['text'] == my_button22['text'] == my_button31['text'] and my_button13['text'] != '': return True
    # Check Vertical
    if my_button11['text'] == my_button21['text'] == my_button31['text'] and my_button11['text'] != '': return True
    elif my_button12['text'] == my_button22['text'] == my_button32['text'] and my_button12['text'] != '': return True
    elif my_button13['text'] == my_button23['text'] == my_button33['text'] and my_button13['text'] != '': return True
    # if !Win return False
    return False

def press(num):
    # Configure Based On Button
    if num == 11: my_button11.configure(text=player, state=DISABLED, font = ('ariel', 9, 'bold'))
    if num == 12: my_button12.configure(text=player, state=DISABLED, font = ('ariel', 9, 'bold'))
    if num == 13: my_button13.configure(text=player, state=DISABLED, font = ('ariel', 9, 'bold'))
    if num == 21: my_button21.configure(text=player, state=DISABLED, font = ('ariel', 9, 'bold'))
    if num == 22: my_button22.configure(text=player, state=DISABLED, font = ('ariel', 9, 'bold'))
    if num == 23: my_button23.configure(text=player, state=DISABLED, font = ('ariel', 9, 'bold'))
    if num == 31: my_button31.configure(text=player, state=DISABLED, font = ('ariel', 9, 'bold'))
    if num == 32: my_button32.configure(text=player, state=DISABLED, font = ('ariel', 9, 'bold'))
    if num == 33: my_button33.configure(text=player, state=DISABLED, font = ('ariel', 9, 'bold'))
    # Check Win Condition
    if winCond():
        winner(player)
    # Else Change Chosen
    else: chosen()
    for client in clients:
        try:
            client.send(f"{num}:{player}".encode())
        except socket.error as e:
            print(f"Error sending data to client: {e}")

def new_game():
    # Activate Buttons & Clear Board
    my_button11.config(state='active', text = "")
    my_button12.config(state='active', text = "")
    my_button13.config(state='active', text = "")
    my_button21.config(state='active', text = "")
    my_button22.config(state='active', text = "")
    my_button23.config(state='active', text = "")
    my_button31.config(state='active', text = "")
    my_button32.config(state='active', text = "")
    my_button33.config(state='active', text = "")
    # Reset Player

    global player
    player = 'X'
    # Will print error First time
    winner_label.destroy()

# Print Out Board
label = Label(root, text="Tic Tac Toe", font=('Ariel', 25), justify='center').grid(row = 0, column=1, columnspan = 4, padx=15, pady=5)
my_button11 = Button(root, command=lambda: press(11), width=6, height=3, state = DISABLED)
my_button11.grid(row=1,column=1, padx=5,pady=5)
my_button12 = Button(root, command=lambda: press(12), width=6, height=3, state = DISABLED)
my_button12.grid(row=1,column=2, padx=5,pady=5)
my_button13 = Button(root, command=lambda: press(13), width=6, height=3, state = DISABLED)
my_button13.grid(row=1,column=3, padx=5,pady=5)
my_button21 = Button(root, command=lambda: press(21), width=6, height=3, state = DISABLED)
my_button21.grid(row=2,column=1, padx=5,pady=5)
my_button22 = Button(root, command=lambda: press(22), width=6, height=3, state = DISABLED)
my_button22.grid(row=2,column=2, padx=5,pady=5)
my_button23 = Button(root, command=lambda: press(23), width=6, height=3, state = DISABLED)
my_button23.grid(row=2,column=3, padx=5,pady=5)
my_button31 = Button(root, command=lambda: press(31), width=6, height=3, state = DISABLED)
my_button31.grid(row=3,column=1, padx=5,pady=5)
my_button32 = Button(root, command=lambda: press(32), width=6, height=3, state = DISABLED)
my_button32.grid(row=3,column=2, padx=5,pady=5)
my_button33 = Button(root, command=lambda: press(33), width=6, height=3, state = DISABLED)
my_button33.grid(row=3,column=3, padx=5,pady=5)
new_game_button = Button(root, text="New Game", font = ('ariel', 10), command=new_game, width = 10, height=2).grid(row = 4, column=1, columnspan=3, pady=5)
exit_button = Button(root, text="Quit", font =('ariel', 10),command=root.quit, width = 10, height=2).grid(row = 5, column=1, columnspan=3, pady=5)

root.mainloop()