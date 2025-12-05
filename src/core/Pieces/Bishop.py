from .Piece import Piece


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B'

    def get_valid_moves(self, board, row, col):
        moves = []
        # Diagonals
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            for i in range(1, 8):
                r, c = row + (dr * i), col + (dc * i)
                
                if not board.is_valid_pos(r, c):
                    break
                
                target = board.grid[r][c]
                if target is None:
                    moves.append((r, c))
                else:
                    if target.color != self.color:
                        moves.append((r, c))
                    break
        return moves