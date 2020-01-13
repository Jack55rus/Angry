from random import randint

class Player:
    def __init__(self, char, pawns):
        self.char = char
        self.pawns = pawns  
        
    def move_pawn(self, index_of_pawn, step):
        self.pawns[index_of_pawn].move(step)
        
    def get_current_pawn_position(self, index_of_pawn):
        self.pawns[index_of_pawn].get_current_position()
        
    def show_pawns_path(self):
        for p in self.pawns:
            print(p.show_pawns_path())
    
    def show_all_pawns_position(self):
        for i, p in enumerate(self.pawns):
            print('idx:', i, 'pos:', p.get_current_position())
    
    def throw_die(self):
        return randint(1, 6)
    