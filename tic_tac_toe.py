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

def play():
    """
    Runs the game loop
    """
    game = Game()
    
    while 1:
        pass

if __name__ == "__main__":
    play()	
