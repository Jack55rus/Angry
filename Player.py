from random import randint, choice

class Player:
    '''
    this class is responsible for any manipulations on the pawns by a player
    '''
    def __init__(self, char, pawns):
        self.char = char # a character that represents the pawns of the palyer
        self.pawns = pawns # a list that consists of the pawns this player owns
        
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
        
    def move_decision(self, current_board, step):
        priors = {} # a proirity dict for the pawns
        for num, chip in enumerate(self.pawns): 
            if not chip.check_in_D(): # if this pawn hasn't reached the D-zone yet
                # print('D check:', chip.check_in_D())
                current_coords = chip.get_current_position() # a tuple so that we can access the board directly using these coords
                potential_new_coords = chip.look_further(step) # a tuple with possible new coords
                potential_content = current_board.get_cell_content(potential_new_coords) # get what is inside the potential cell
                if potential_content == self.char: # if the player's another pawn is located at the potential position, consider other options
                    continue
                if current_coords is None and step != 6:
                    continue
                priors.update({num:[]}) # add index of the pawn as a key to the priority dict
                cond_1 = potential_content == 'D' # 1st prior: the pawn is able to advance to the D-zone
                if cond_1:
                    priors[num].append(1)
                cond_2 = (potential_content != self.char and potential_content != '*') # 2nd prior: the pawn can eject an opponent's pawn
                if cond_2:
                    priors[num].append(2)
                cond_3 = current_coords is None # 3rd prior: the pawn is not activated
                if cond_3:
                    priors[num].append(3)
                if not cond_1 and not cond_2 and not cond_3: # 4th prior: neither of the previous ones
                    priors[num].append(4)
                    
        min_val = 5 # value greater than the max possible priority
        min_keys = list() # list containing indices of the pawns that have smallest priorities
        # this block chooses the min priority for each pawn and then chooses min priority among all pawns
        if len(priors) > 0: # if at least one pawn can be moved
            for pawns_ind in priors: # for all active pawns
                M = min(priors[pawns_ind]) # calc min prior for this particular pawn
                if M <= min_val: # and if the newly calculated min value is less than the current one
                    min_val = M # assign min val to this number
                    # min_keys.append(pawns)
            for pawns_ind in priors: # go through all pawns 
                if min_val in priors[pawns_ind]: # chick whether min val in this pawn's prior list
                    min_keys.append(pawns_ind) # add index of this pawn to the lsit that contains min keys
        else: # if there are no pawns that can be moved, return -1's. Note: this condition must be handled from outside
            return -1, -1, -1
        
        print('min_keys list', min_keys)
        if len(min_keys) != 0: # if the previous list is not empty (i.e. more than one pawn share min keys)
            chosen_pawn_ind = choice(min_keys) # make a random choice to define which of them to be moved
            # self.move_pawn(chosen_pawn_ind, step) # commented for now as I suppose this method should only make a decision rather than actions
            previous_coords = self.pawns[chosen_pawn_ind].get_current_position() # get previous coords of the pawn we decided to move
            potential_returned_coords = self.pawns[chosen_pawn_ind].look_further(step) # get its new coords
            returned_index = chosen_pawn_ind # index of the pawn we'll move
        else:
            previous_coords = self.pawns[min_keys[0]].get_current_position() # if only pawn can be moved
            potential_returned_coords = self.pawns[min_keys[0]].look_further(step) # get its new coords
            returned_index = min_keys[0]
        print('previous_coords', previous_coords)
        print('potential_returned_coords', potential_returned_coords)
        
        return returned_index, previous_coords, potential_returned_coords
                
    