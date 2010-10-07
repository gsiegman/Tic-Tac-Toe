class Player(object):
    """
    A Tic-Tac-Toe Player
    """
    SYMBOLS = ('X', 'O',)
    PLAYER_TYPES = ('human', 'computer',)
    
    def __init__(self, symbol, player_type, game):
        if symbol not in self.SYMBOLS: 
            # better validation could be done to
            # ensure uniqueness to other player
            raise Exception(
                "Invalid game symbol, must be 'X' or 'O'."
            )
        
        self.symbol = symbol
        
        if player_type not in self.PLAYER_TYPES:
            raise Exception(
                "Invalid player type, must be 'human' or 'computer'"
            )
        
        self.player_type = player_type
        self.game = game
        
    def play(self):
        getattr(self, '%s_play' % self.player_type)()
    
    def human_play(self):
        while True:
            play_spot = raw_input("Please enter your move: ")
            if self.game.is_valid_play(play_spot):
                self.game.board[self.game.board.index(play_spot)] = self.symbol
                self.game.display_board()
                break
            else:
                self.game.display_board()
        
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
        
        #used as game terminator if
        #even if there isn't a winner
        self.valid_moves_count = 0
    
    def display_board(self):
        rows = [self.board[0:3], self.board[3:6], self.board[6:9]]
        
        for row in rows:
            print ' '.join(row)
            
    def is_valid_play(self, play_spot):
        if str(play_spot) not in self.board:
            print 'Invalid play, please select another spot.'
            return False
        
        self.valid_moves_count += 1
        return True
        
    def is_game_over(self):
        # need to add check for winning condition when
        # completed.
        return self.valid_moves_count == 9
        print 'Game over.'

def play():
    """
    Runs the game loop
    """
    game = Game()
    game.display_board()
    
    player_1 = Player('X', 'human', game)
    player_2 = Player('O', 'human', game)
	
    while 1:
        player_1.play()
        if game.is_game_over():
            break
        
        player_2.play()
        if game.is_game_over():
            break

if __name__ == "__main__":
    play()	
