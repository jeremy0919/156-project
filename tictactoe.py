class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(9)]  # we will use a single list to rep 3x3 board
        self.player_symbol = ['X', 'O']   # keep track of which player goes first
        self.win_combos = [    # all possible winning combos
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 4, 8],
            [2, 4, 6],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8]
        ]
        self.player = 0    # keep track of winner

    def addPlayer(self, player):
        self.player = player                          # add player to game

    def go2OthPlayer(self):
        return 1 if self.player == 0 else 0            # return the other player

    def validMove(self, move):
        return 0 <= move < 9 and self.board[move] == ' '

    def makeMove(self, move, player):
        if self.validMove(move):
            self.player_symbol = 'X' if player == 1 else 'O'
            self.board[move] = self.player_symbol
            self.player = self.go2OthPlayer()
        else:
            print("Invalid move!")
    def help():
        print("How do yuo not know how to play tictactoe")
    def isWinner(self, player):                        # check if player has won
        for combo in self.win_combos:
            if all(self.board[i] == self.player_symbol[player - 1] for i in combo): # check if player has all 3 in a row
                return True
        return False

    def isBoardFull(self):
        return all(i != ' ' for i in self.board)         # check if board is full
    
    def restart(self):
        self.board = [' ' for _ in range(9)]
        self.player = 0
   # def show(self):
        #print("-------------")
    #    print("\n\n")
     #   for i in range(0, 9, 3):
    #        row = " | ".join(self.board[i:i + 3])
     #       print(f"  {row}  ")
      #      if i < 6:
      #          print("-------------")
    def update_board(self, move, player):
        if 0 <= move < 9 and self.board[move] == ' ':
            self.board[move] = self.player_symbol[player - 1]

    def show_updated_board(self):
        print("\n\n")
        for i in range(0, 9, 3):
            row = " | ".join(self.board[i:i + 3])
            print(f"  {row}  ")
            if i < 6:
                print("-------------")
    def show():
        print("its tic tac toe yall are really keeping score ")
    def showWinner():
        print("you really cant see who got three in a row smhhh")