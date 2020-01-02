class Pawn:
	'''
	just a notation clarification: pawn = chip
	The Pawn class handles any manipulation on the pawns produced by a player
	'''
    def __init__(self, char, path, board):
        self.char = char # a character the pawn is represented by 
        self.path = path(board, char) # Path class
        self.current_position_idx = 0 # None by default
    
    def show_pawns_path(self):
        return self.path.get_path() # display the whole path for the pawn
    
    def move(self, step):
        self.current_position_idx += step 
        
    def get_current_position(self):
        return self.path.get_path()[self.current_position_idx]
        
    def is_in_D(self):
		# check if the pawn is in D-field already
        return False if self.current_position_idx < len(self.path.get_path()) - self.Ds - 1 else True
        
    def back_home(self):
		# send the pawn back to the home area. Necessary when a pawn is suspended by the opponent's one
        self.current_position_idx = 0
        
    
    