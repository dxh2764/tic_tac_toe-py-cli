import math

class Board():
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]


    def print_board(self):
        def replace_none(value):
            return " " if value is None else value

        for row in self.board:
            print(list(map(replace_none, row)))

    def get_index(self, position):
        row_index = math.ceil(position / 3) - 1
        col_index = 2 if (position % 3 - 1) == -1 else (position % 3 - 1)
        return [row_index, col_index]

    def add_piece(self, piece, position):
        row_index, col_index = self.get_index(position)
        self.board[row_index][col_index] = piece

    def valid_position(self, position):
        if position not in range(1, 10):
            return f'Invalid position: {position}. Enter a position within 1 through 9'

        row_index, col_index = self.get_index(position)

        if self.board[row_index][col_index]:
            return f'The position {position}, is already filled'
    
    def full_board(self):
        for row in self.board:
            for col in row:
                if col == None: return False
        return True

    def horizontal(self):
        for row in self.board:
            if (row[0] and row[0] == row[1] and row[1] == row[2]): 
                return True
        return False

    def vertical(self):
        for col_index in range(3):
            if (self.board[0][col_index]
                and self.board[0][col_index] == self.board[1][col_index]
                and self.board[1][col_index] == self.board[2][col_index]): 
                return True
        return False
    
    def diagonal(self):
        if not self.board[1][1]: 
            return False
        if self.board[0][0] == self.board[1][1] and self.board[2][2] == self.board[1][1]: 
            return True
        if self.board[2][0] == self.board[1][1] and self.board[0][2] == self.board[1][1]: 
            return True
        return False
    
    def winning_state(self):
        return self.horizontal() or self.vertical() or self.diagonal()
            
