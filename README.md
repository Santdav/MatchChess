# Match chess
**Match Chess** is a modular, Python-based chess engine designed for architectural flexibility. Unlike standard engines optimized purely for speed, Chimera is optimized for extensibility, allowing for the easy creation of custom pieces, non-standard board sizes, and experimental rule sets.

## Architecture
The project follows a strict Model-View-Controller (MVC) pattern to ensure the logic remains separate from the rendering:

Core (Model): Handles the 8x8 grid (object-based) and piece definitions.

GUI (View): Uses PyGame to render the state.

AI (Strategy): Pluggable agent system (Human vs. Human, Human vs. Bot).

## Roadmap & Progress
### Phase 1: The Skeleton (Console & Basics)

[ ] Setup project folder structure

[ ] Create base Piece class (Color, Position, ID)

[ ] Create Board class (8x8 Grid populated with None)

[ ] Implement Pawn movement logic (basic push)

[ ] Implement King movement logic (1 step radius)

[ ] Create a Text/Console Renderer (print board to terminal)

[ ] Milestone: Move a Pawn and King around in the terminal.

### Phase 2: The Standard Army

[ ] Implement Rook logic (sliding horizontal/vertical)

[ ] Implement Bishop logic (sliding diagonal)

[ ] Implement Queen logic (combined Rook/Bishop)

[ ] Implement Knight logic (L-shape jumps)

[ ] Implement Collision Detection (sliding pieces blocked by others)

[ ] Implement Basic Capturing (replace enemy piece on target square)

[ ] Milestone: A playable game in console (ignoring Checks).

### Phase 3: The Referee (Rules Engine)

[ ] Implement Turn Management (White -> Black -> White)

[ ] Implement Move class (Command Pattern for Undo/Redo)

[ ] Add Undo functionality

[ ] Implement FEN String parsing (Load custom board states)

[ ] Implement Check detection (Is the King under attack?)

[ ] Implement Checkmate & Stalemate detection

[ ] Add Special Moves: Castling

[ ] Add Special Moves: En Passant

[ ] Add Special Moves: Pawn Promotion

### Phase 4: The Visuals (GUI)

[ ] Initialize PyGame window

[ ] Draw the Checkerboard (dynamic resizing)

[ ] Load and blit Piece sprites (Images)

[ ] Implement Mouse Drag-and-Drop

[ ] Add visual highlights for "Valid Moves"

[ ] Add Sound Effects

### Phase 5: The Artificial Intelligence

[ ] Create RandomBot (picks valid moves at random)

[ ] Implement Material Evaluation (Pawn=1, Rook=5, etc.)

[ ] Implement Minimax Algorithm (Recursive search)

[ ] Implement Alpha-Beta Pruning (Optimization)

[ ] Milestone: Beating the bot.

### Phase 6: The Chimera (Customization)

[ ] Refactor Board to support non-8x8 grids

[ ] Create a Custom Piece (e.g., The "Wizard" or "Cannon")

[ ] Create a Custom Board Setup

## Usage
```console
pip install -r requirements.txt
```
```python
python src/main.py
```