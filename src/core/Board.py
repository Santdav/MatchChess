from .Pieces.Pawn import Pawn
from .Pieces.Rook import Rook
from .Pieces.Knight import Knight
from .Pieces.Bishop import Bishop
from .Pieces.Queen import Queen
from .Pieces.King import King

class Board:
    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def is_valid_pos(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_empty(self, row, col):
        return self.grid[row][col] is None

    def setup_standard(self):
        """
        Sets up the standard Chess board.
        White is at the bottom (rows 6, 7), Black at top (rows 0, 1).
        """
        # 1. Pawns
        for col in range(8):
            self.grid[6][col] = Pawn('white')
            self.grid[1][col] = Pawn('black')

        # 2. Main Pieces
        # Order: Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook
        # Note: King is on E (col 4), Queen on D (col 3)
        #TODO fix order of queen and king
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for col, PieceClass in enumerate(piece_order):
            self.grid[7][col] = PieceClass('white')
            self.grid[0][col] = PieceClass('black')

    def move_piece(self, start_pos, end_pos):
        r1, c1 = start_pos
        r2, c2 = end_pos

        piece = self.grid[r1][c1]
        if not piece:
            print(f"Error: No piece at {start_pos}")
            return False

        # Ask the piece if the move is theoretically valid
        valid_moves = piece.get_valid_moves(self, r1, c1)
        
        if (r2, c2) not in valid_moves:
            print(f"Error: Illegal move for {piece.symbol} to {end_pos}")
            return False

        # Execute Move
        # Note: This overwrites whatever is at r2, c2 (Capturing logic)
        self.grid[r2][c2] = piece
        self.grid[r1][c1] = None
        
        # Flag update (useful for Pawn first move or Castling later)
        piece.has_moved = True
        
        return True