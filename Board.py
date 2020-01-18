import numpy as np

class Board:
    '''
    Creates a board for 4 players with a given number of cells. 
    
    '''
    def __init__(self, n):
        ''' 
        creates an empty numpy array that will be filled in create_board
        n: number of cells along an axis (the board is square)
        '''
        self.n = n
        self.board = np.empty((self.n, self.n), dtype=str)
    
    def create_board(self):
        '''
        fills the board that was initiated in __init__
        '''
        self.board = np.empty((self.n, self.n), dtype=str)
        E = (self.n-3)/2
        for i in range(0, self.n):
            for j in range(0, self.n):
                if (i-E<0 and j-E<0) or (i+E>self.n-1 and j+E>self.n-1) or (i+E>self.n-1 and j-E<0) or (i-E<0 and j+E>self.n-1):
                    self.board[i][j] = ' '
                elif i==(self.n-1)/2 and j==(self.n-1)/2:
                    self.board[i][j] = 'X'
                elif (i==(self.n-1)/2 and (j!=0 and j!=self.n/2 and j!=self.n-1)) or (j==(self.n-1)/2 and (i!=0 and i!=self.n/2 and i!=self.n-1)):
                    self.board[i][j] = 'D'
                else:
                    self.board[i][j] = '*'
                    
        
    def update_board(self, prev_coords, new_coords, char):
        if prev_coords is None:
            self.board[new_coords[0]][new_coords[1]] = char
        elif prev_coords is not None and new_coords is None:
            self.board[prev_coords[0]][prev_coords[1]] = '*'
        elif prev_coords is not None and new_coords is not None:
            self.board[prev_coords[0]][prev_coords[1]] = '*'
            self.board[new_coords[0]][new_coords[1]] = char
    
    def show_board(self):
        '''
        displays current state of the board without the indices
        '''
        for i in range(0, self.n):
            for j in range(0, self.n+1):
                if j == self.n:
                    print('\n')
                else:
                    print(self.board[i][j], end='   ')
    
    def show_board_numbers(self):
        '''
        displays current state of the board w/the indices
        '''
        board2show = np.empty((self.n+1, self.n+1), dtype=str)
        board2show[1:, 1:] = self.board
        board2show[0][0] = ' '
        board2show[1:, 0] = list(range(self.n))
        board2show[0, 1:] = list(range(self.n))
        for i in range(0, self.n+1):
            for j in range(0, self.n+1+1):
                if j == self.n+1:
                    print('\n')
                else:
                    print(board2show[i][j], end='   ')
    
    def get_board(self):
        return self.board