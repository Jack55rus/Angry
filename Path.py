import numpy as np

class Path:
    '''
    path class is used to construct a game path for a particular pawn 
    
    '''
    def __init__(self, board, char):
        ''' board: current baord (Board class)
        char: a letter 
        '''
        self.char = char
        self.board = np.copy(board.get_board())
        self.path = []
        self.n = len(self.board)
        self.p = int((self.n-3)/2) # number of pawns = # number of D-spots
        
    '''
    the 4 functions below (move_down, -right, -left, -up) are the private ones to pave the way for the pawns
    they just scan the board consecutively finding *'s  
    '''
    def __move_down(self, i, j, temp_path, D=False):
        check_symbol = '*' if not D else 'D'
        while self.board[i][j] == check_symbol: # while it's asterisk, we move down 
            temp_path.append((i, j))
            i += 1
            if i >= self.n: # allows to avoid going away from the board
                break
        i -= 1
        return i, j
    
    def __move_right(self, i, j, temp_path, D=False):
        check_symbol = '*' if not D else 'D'
        while self.board[i][j] == check_symbol:
            temp_path.append((i, j))
            j += 1
            if j >= self.n:
                break
        j -= 1
        return i, j
    
    def __move_left(self, i, j, temp_path, D=False):
        check_symbol = '*' if not D else 'D'
        while self.board[i][j] == check_symbol:
            temp_path.append((i, j))
            j -= 1
            if j < 0:
                break
        j += 1
        return i, j
    
    def __move_up(self, i, j, temp_path, D=False):
        check_symbol = '*' if not D else 'D'
        while self.board[i][j] == check_symbol:
            temp_path.append((i, j))
            i -= 1
            if i < 0:
                break
        i += 1
        return i, j
    
    def create_path(self):
#         p = int((self.n-3)/2) # number of pawns
        A = (0, self.n-1-self.p) # initial coordinates for player A
        B = (self.n-1, self.p) # initial coordinates for player B
        C = (self.n-1-self.p, self.n-1)
        E = (self.p, 0)
        i = A[0]
        j = A[1]
        dots = 8*(self.p+1)
        starting_dot_A = 0
        starting_dot_B = int(dots/2) # starts from the half of the board
        starting_dot_C = int(dots/4) # ...
        starting_dot_E = int(dots/(4/3))
        path = []
        path.append((A[0], A[1]))
        i += 1
        i, j = self.__move_down(i, j, path)
        j += 1
        i, j = self.__move_right(i, j, path)
        i += 1
        i, j = self.__move_down(i, j, path)
        j -= 1
        i, j = self.__move_left(i, j, path)
        i += 1
        i, j = self.__move_down(i, j, path)
        j -= 1
        i, j = self.__move_left(i, j, path)
        i -= 1
        i, j = self.__move_up(i, j, path)
        j -= 1
        i, j = self.__move_left(i, j, path)
        i -= 1
        i, j = self.__move_up(i, j, path)
        j += 1
        i, j = self.__move_right(i, j, path)
        i -= 1
        i, j = self.__move_up(i, j, path)
        j += 1
        i, j = self.__move_right(i, j, path)
        j -= 1
        ###
        D_field = []
        ###
        actual_path = [(0, 0)]*dots
        if self.char == 'A':
            actual_path = path[:len(path)-1]
            i, j = actual_path[-1]
            # print(i, j)
            self.__move_down(i+1, j, D_field, D=True)
            actual_path += D_field
            actual_path.insert(0, None)
        elif self.char == 'B':
            actual_path[0] = (B[0], B[1])
            actual_path[1:starting_dot_B] = path[starting_dot_B+1:]
            actual_path[starting_dot_B:] = path[:starting_dot_B]
            i, j = actual_path[-1]
            self.__move_up(i-1, j, D_field, D=True)
            actual_path += D_field
            actual_path.insert(0, None)
        elif self.char == 'C':
            actual_path[0] = (C[0], C[1]) # starting_dot_C = 8
            actual_path[1:dots-starting_dot_C] = path[starting_dot_C+1:] 
            actual_path[dots-starting_dot_C:] = path[:starting_dot_C] 
            i, j = actual_path[-1]
            self.__move_left(i, j-1, D_field, D=True)
            actual_path += D_field
            actual_path.insert(0, None)
        elif self.char == 'E':
            actual_path[0] = (E[0], E[1])
            actual_path[1:dots-starting_dot_E] = path[starting_dot_E+1:]
            actual_path[dots-starting_dot_E:] = path[:starting_dot_E]
            i, j = actual_path[-1]
            self.__move_right(i, j+1, D_field, D=True)
            actual_path += D_field
            actual_path.insert(0, None)
        '''
        inserting None simulates 'the home' area
        this is done to avoid creating another class (e.g. Box or Home)
        furthermore, it allows to return a suspended pawn just by passing a negative argument to the move method
        '''
        return actual_path
    
    def get_path(self):
        self.path = self.create_path()
        return self.path