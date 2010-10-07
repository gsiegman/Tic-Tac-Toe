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
        
        self.played = []

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
	
    while 1:
        pass

if __name__ == "__main__":
    play()	
