import Piece
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color) # Run the Parent setup first
        self.symbol = 'P'

    def get_valid_moves(self, board, row, col):
        moves = []
        # White moves UP (-1), Black moves DOWN (+1)
        direction = -1 if self.color == 'white' else 1

        ## ToDO: Implement En Passant and Promotion later
        ## ToDO: Implement 2-step move on first move
        
        # 1. Standard Move (1 Step Forward)
        next_row = row + direction
        if board.is_valid_pos(next_row, col):
            #p We can only move forward if the spot is emty
            if board.is_empty(next_row, col):
                moves.append((next_row, col))

        # 2. Capturing (Diagonal)
        # Pawns capture diagonally left (-1) and right (+1)
        for d_col in [-1, 1]:
            capture_col = col + d_col
            if board.is_valid_pos(next_row, capture_col):
                target = board.grid[next_row][capture_col]
                # If there is a piece and it's the ENEMY
                if target and target.color != self.color:
                    moves.append((next_row, capture_col))

        return moves