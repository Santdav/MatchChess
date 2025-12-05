from .Piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R'

    def get_valid_moves(self, board, row, col):
        moves = []
        # Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            for i in range(1, 8):  # Max distance is 7 squares
                r, c = row + (dr * i), col + (dc * i)
                
                if not board.is_valid_pos(r, c):
                    break  # Off board
                
                target = board.grid[r][c]
                if target is None:
                    moves.append((r, c))
                else:
                    # Hit a piece
                    if target.color != self.color:
                        moves.append((r, c))  # Capture
                    break  # Blocked by piece (friend or foe)
        return moves