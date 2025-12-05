from .Piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K'

    def get_valid_moves(self, board, row, col):
        moves = []
        # King can move 1 step in any direction (8 squares around him)
        possible_steps = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for d_row, d_col in possible_steps:
            new_row, new_col = row + d_row, col + d_col
            
            if board.is_valid_pos(new_row, new_col):
                target = board.grid[new_row][new_col]
                # Move if empty OR capture enemy
                if target is None or target.color != self.color:
                    moves.append((new_row, new_col))
        
        return moves