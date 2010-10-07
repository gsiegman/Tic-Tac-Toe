class Player(object):
    """
    A Tic-Tac-Toe Player
    """
    SYMBOLS = ('X', 'O',)
    PLAYER_TYPES = ('human', 'computer',)
    
    def __init__(self, symbol, type):
        if symbol not in self.SYMBOLS: 
            # better validation could be done to
            # ensure only uniqueness to other
            # player
            raise Exception(
                "Invalid game symbol, must be 'X' or 'O'."
            )
        
        self.symbol = symbol
        
        if type not in self.PLAYER_TYPES:
            raise Exception(
                "Invalid player type, must be 'human' or 'computer'"
            )
        
        self.type = type
        
    def play(self):
        if self.type == 'human':
            self.human_play()
        elif self.type == 'computer':
            self.computer_play()
        else:
            raise Exception('Invalid Player Type')
        
    def human_play(self):
        print 'human played'
        
    def computer_play(self):
        print 'computer played'
        
class Game(object):
    """
    A Game of Tic-Tac-Toe
    """
    WINNING_COMBINATIONS = [
    	[1, 2, 3], [4, 5, 6],
    	[7, 8, 9], [1, 4, 7],
    	[2, 5, 8], [3, 6, 9],
    	[1, 5, 9], [3, 5, 7],
    ]
    
    def __init__(self):
        self.board = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9'
        ]

    def display_board(self):
        rows = [self.board[0:3], self.board[3:6], self.board[6:9]]
        
        for row in rows:
            print ' '.join(row)

def play():
    """
    Runs the game loop
    """
    game = Game()
    game.display_board()
    
    player_1 = Player('X', 'human')
    player_2 = Player('O', 'computer')
	
    while 1:
        player_1.play()
        player_2.play()
        break

if __name__ == "__main__":
    play()	
