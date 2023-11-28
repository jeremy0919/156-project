class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(10)]  # we will use a single list to rep 3x3 board
        self.player_symbol = ['X', 'O']   # keep track of which player goes first
        self.win_combos = [    # all possible winning combos
            
             # #off of 1-9 gives a zero error
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [1, 5, 9],
             [3, 5, 7],
             [1, 4, 7],
             [2, 5, 8],
             [3, 6, 9]
            
            # #off of 0-8 gives error with 9(8)
            #  [0, 1, 2],
            #  [3, 4, 5],
            #  [6, 7, 8],
            #  [0, 4, 8],
            #  [2, 4, 6],
            #  [0, 3, 6],
            #  [1, 4, 7],
            #  [2, 5, 8]
            
        
        ]
        self.player = 0    # keep track of winner

    def addPlayer(self, player):
        self.player = player                          # add player to game

    def go2OthPlayer(self):
        return 1 if self.player == 0 else 0            # return the other player

    def validMove(self, move, player):
        return 1 <= move <= 9 and self.board[move] == ' '
    def makeMove(self, move, player):
        self.board[move - 1] = self.player_symbol[player - 1]
        self.player = self.go2OthPlayer() 
    def isWinner(self, player):                        # check if player has won
        for combo in self.win_combos:
            if all(self.board[i] == self.player_symbol[player - 1] for i in combo): # check if player has all 3 in a row
                return True
        return False

    def isBoardFull(self):
        return all(i != ' ' for i in self.board)         # check if board is full
    
    def restart(self):
        self.board = [' ' for _ in range(10)]
        self.player = 0
    def show(self):
        #print("-------------")
        print("\n\n")
        for i in range(0, 9, 3):
            row = " | ".join(self.board[i:i + 3])
            print(f"  {row}  ")
            if i < 6:
                print("-------------")
