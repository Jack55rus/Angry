class Pawn:
    def __init__(self, char, path, board):
        self.char = char
        self.path = path(board, char) # Path class
        self.current_position_idx = 0
#         self.start_position = self.path.get_path()[0]
    
    def show_pawns_path(self):
        return self.path.get_path()
    
    def move(self, step):
        self.current_position_idx += step
        
    def get_current_position(self):
        return self.path.get_path()[self.current_position_idx]
