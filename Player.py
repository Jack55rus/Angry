from random import randint

class Player:
    '''
    this class is responsible for any manipulations on the pawns by a player
    '''
    def __init__(self, char, pawns):
        self.char = char # a character that represents the pawns of the palyer
        self.pawns = pawns  # a list that consists of the pawns this player owns
        
    def move_pawn(self, index_of_pawn, step):
        self.pawns[index_of_pawn].move(step)
        
    def get_current_pawn_position(self, index_of_pawn):
        return self.pawns[index_of_pawn].get_current_position()
        
    def show_pawns_path(self):
        for p in self.pawns:
            print(p.show_pawns_path())
    
    def show_all_pawns_position(self):
        for i, p in enumerate(self.pawns):
            print('idx:', i, 'pos:', p.get_current_position())
    
    def throw_die(self):
        return randint(1, 6)
    
    def eject_own_pawn(self, index_of_ejected_pawn):
        self.pawns[index_of_ejected_pawn].back_home()
    