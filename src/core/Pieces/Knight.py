import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'N' # Standard chess notation for Knight is N

    def get_valid_moves(self, board, row, col):
        moves = []
        # L-shapes: 2 in one direction, 1 in the other
        jumps = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2),  (1, 2),  (2, -1),  (2, 1)
        ]

        for dr, dc in jumps:
            r, c = row + dr, col + dc
            
            if board.is_valid_pos(r, c):
                target = board.grid[r][c]
                if target is None or target.color != self.color:
                    moves.append((r, c))
        return moves