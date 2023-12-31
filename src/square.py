
class Square:

    ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, row, col, piece=None): # Optional parameter piece - Not all squares are going to have a chess piece on it.
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacol = self.ALPHACOLS[col]

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        return self.piece != None
    
    def isempty(self):
        return not self.has_piece()

    def has_team_piece(self, colour):
        return self.has_piece() and self.piece.colour == colour

    def has_rival_piece(self, colour):
        return self.has_piece() and self.piece.colour != colour

    def isempty_or_rival(self, colour):
        return self.isempty() or self.has_rival_piece(colour)
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False 
        return True

    @staticmethod 
    def get_alphacol(col):
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALPHACOLS[col]

"""
print(Square.in_range(1,2,3,4,9)) # => False as 9 is outside the range of 0 ≤ arg ≤ 7.
print(Square.in_range(1,2,3,4,9)) # => True as the numbers 1, 2, 3 and 4 are inside the range of 0 ≤ arg ≤ 7.
"""