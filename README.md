# Tetris Game

A classic Tetris implementation built with Python and Pygame. Experience the timeless puzzle game with smooth controls, line clearing mechanics, and progressive difficulty levels.

## 🎮 Features

- **Classic Tetris Gameplay**: All 7 traditional tetromino pieces (I, O, T, S, Z, J, L)
- **Smooth Controls**: Responsive keyboard input for movement and rotation
- **Line Clearing**: Complete horizontal lines disappear and award points
- **Progressive Difficulty**: Game speed increases with each level
- **Score System**: Points awarded based on lines cleared simultaneously
- **Real-time UI**: Live display of score, level, and lines cleared
- **Collision Detection**: Proper boundary and piece collision handling

## 🎯 Game Controls

| Key | Action |
|-----|--------|
| ← | Move piece left |
| → | Move piece right |
| ↓ | Move piece down (soft drop) |
| ↑ | Rotate piece clockwise |
| ESC | Exit game |

## 📋 Requirements

- Python 3.6 or higher
- Pygame library

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KrishnoMD305/Tetris-Game.git
   cd tetris-game
   ```

2. **Install Pygame:**
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```
   

## 🎲 How to Play

1. **Objective**: Clear horizontal lines by filling them completely with falling tetromino pieces
2. **Piece Movement**: Use arrow keys to move and rotate falling pieces
3. **Line Clearing**: When a horizontal line is completely filled, it disappears and you score points
4. **Level Progression**: Clear 10 lines to advance to the next level
5. **Game Over**: The game ends when pieces stack up to the top of the playing field

## 📊 Scoring System

| Lines Cleared | Base Points |
|---------------|-------------|
| 1 line | 100 points |
| 2 lines | 200 points |
| 3 lines | 500 points |
| 4 lines (Tetris) | 800 points |

**Final Score = Base Points × Current Level**

## 🏗️ Game Architecture

### Core Classes

- **`TetroMino`**: Represents individual falling pieces
  - Handles piece rotation and position
  - Manages piece shapes and colors
  - Calculates occupied cell positions

- **`TetrisGame`**: Main game engine
  - Manages game state and logic
  - Handles user input and events
  - Controls piece movement and collision detection
  - Manages scoring and level progression

### Key Features Implementation

- **Collision Detection**: Prevents pieces from overlapping or moving outside boundaries
- **Line Clearing Algorithm**: Efficiently removes complete lines and shifts remaining blocks
- **Rotation System**: Smooth piece rotation with collision validation
- **Fall Speed Progression**: Automatic speed increase based on player level

## 🎨 Game Specifications

- **Grid Size**: 10×20 cells
- **Cell Size**: 30×30 pixels
- **Window Size**: 800×700 pixels
- **Frame Rate**: 60 FPS
- **Starting Fall Speed**: 1000ms per cell
- **Speed Increase**: 50ms faster per level

## 🔧 Customization

You can easily modify the game by adjusting constants in the code:

```python
# Window and grid dimensions
window_height = 700  
window_weidth = 800
grid_weidth = 10
grid_height = 20
cellsize = 30

# Game speed
fall_speed = 1000  # milliseconds

# Colors for each piece type
Pieces = {
    "I": {"color": Cyan},
    "O": {"color": Yellow},
    # ... etc
}
```

## 🐛 Known Issues

- Game over message appears in terminal only
- No pause functionality
- No save/load game state



## 📞 Contact

If you have any questions, suggestions, or issues, please feel free to open an issue on GitHub or contact me directly.

---

**Enjoy the game and happy stacking! 🧱**
