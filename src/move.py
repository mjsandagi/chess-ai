
class Move:
    def __init__(self, initial, final): # I shall deign to share this dance with you.
        # initial and final are squares, not tuples.
        self.initial = initial
        self.final = final

    def __str__(self):
        s = ""
        s += f"({self.initial.col}, {self.initial.row})"
        s += f"({self.final.col}, {self.final.row})"
        return s
    
    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final