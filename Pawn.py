class Pawn:
    '''
    just a notation clarification: pawn = chip
    The Pawn class handles any manipulation on the pawns produced by a player
    '''
    def __init__(self, char, path):
        self.char = char # a character the pawn is represented by 
        self.path = path # Path class
        self.current_position_idx = 0 # None by default
        self.Ds = self.path.p
        self.is_in_D = False
    
    def show_pawns_path(self):
        return self.path.get_path() # display the whole path for the pawn
    
    def move(self, step):
        # self.check_in_D()
        if self.check_in_D():
            self.current_position_idx += 0
            print('this pawn has already reached the D-zone')
        elif self.current_position_idx + step >= len(self.path.get_path()):
            self.current_position_idx += 0
            print('this pawn cannot be moved since it will go outside in this case')
        else:
            self.current_position_idx += step 
        
    def get_current_position(self):
        return self.path.get_path()[self.current_position_idx]
        
    def check_in_D(self):
        # check if the pawn is in D-field already
        # print('entered check_in_D')
        # print('self.current_position_idx', self.current_position_idx, 'len(self.path.get_path())', len(self.path.get_path()), 'self.Ds', self.Ds)
        # print('self.is_in_D', self.is_in_D)
        # self.is_in_D = True if self.current_position_idx >= len(self.path.get_path()) - self.Ds else False
        if self.current_position_idx >= len(self.path.get_path()) - self.Ds:
            self.is_in_D = True
            return True
        else:
            self.is_in_D = False
            return False
        
    def back_home(self):
        # send the pawn back to the home area. Necessary when a pawn is suspended by the opponent's one
        self.current_position_idx = 0
        
    def look_further(self, how_far):# look what is located how_far steps away from the current pawn
        if self.current_position_idx + how_far >= self.path.get_path_len():
            return self.path.get_path()[self.current_position_idx]
        return self.path.get_path()[self.current_position_idx + how_far]
    