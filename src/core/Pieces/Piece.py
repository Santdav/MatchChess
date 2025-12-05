from abc import ABC

class Piece(ABC):
    """
    The Parent class. All pieces (standard or custom) inherit from this.
    """
    def __init__(self, color):
        self.color = color  # 'white' or 'black'
        self.symbol = 'BASE PIECE'   # We will overwrite this (e.g., 'P', 'K')
        self.has_moved = False # Useful for Castling later

    def get_valid_moves(self, board, row, col):
        """
        The Rulebook. Every piece must implement this method.
        It returns a list of tuples: [(5, 0), (5, 1)]
        """
        raise NotImplementedError("This is a template. Subclasses must define their own movement.")

    def __str__(self):
        # This controls how the piece prints in the terminal
        # 'wP' for White Pawn, 'bK' for Black King
        return f"{self.color[0]}{self.symbol}"
