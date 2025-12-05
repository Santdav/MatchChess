import sys
import os
sys.path.append(os.getcwd())
from core.Board import Board
# Ensure python can find our modules


# Removed the external renderer import to keep things simple

def parse_input(input_str):
    """Converts 'row,col' string to (row, col) tuple."""
    try:
        parts = input_str.split(',')
        if len(parts) != 2:
            return None
        r, c = map(int, parts)
        return r, c
    except ValueError:
        return None

def print_simple_board(board):
    """
    A simple function to log the board state to the console.
    It iterates over the grid and prints the piece symbols.
    """
    print("\n   0  1  2  3  4  5  6  7")
    print("  ------------------------")
    for r in range(board.rows):
        line = f"{r}|"
        for c in range(board.cols):
            piece = board.grid[r][c]
            if piece:
                # Print 'wP' for White Pawn, 'bK' for Black King, etc.
                line += f" {piece.color[0]}{piece.symbol}"
            else:
                line += " . " # Empty square
        print(line)
    print("\n")

def main():
    # 1. Initialize the Game
    game_board = Board()
    
    # Use standard setup
    game_board.setup_standard()
    
    turn = 'white' 

    print("--- Project Chimera: Simple Console Test ---")
    print("Commands: Type coordinates as 'row,col'. Example: '6,4'")

    while True:
        # 2. Log the Board to Console
        print_simple_board(game_board)

        # 3. Input Phase
        print(f"[{turn.upper()}'s Turn]")
        try:
            start_str = input("Select Piece to Move (r,c): ")
            start_pos = parse_input(start_str)
            
            target_str = input("Select Target Square (r,c): ")
            target_pos = parse_input(target_str)

            if not start_pos or not target_pos:
                print(">> Invalid format. Use 'row,col'")
                continue

            # Basic Validation
            start_piece = game_board.grid[start_pos[0]][start_pos[1]]
            
            if not start_piece:
                print(">> No piece there!")
                continue

            if start_piece.color != turn:
                print(f">> Not your piece!")
                continue

            # 4. Update Phase
            if game_board.move_piece(start_pos, target_pos):
                print(f">> Move successful.")
                turn = 'black' if turn == 'white' else 'white'
            else:
                print(">> Move failed (Illegal move).")

        except KeyboardInterrupt:
            print("\nGame Exited.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()