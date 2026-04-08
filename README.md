# Project-21

# Turtle Crossing Game 🐢🚗

A Frogger-style game where you help a turtle cross a busy road while avoiding colorful cars. Each level gets progressively harder!

## Project Structure
turtle-crossing/
│
├── main.py           # Main game loop and controls
├── player.py         # Player (turtle) class
├── car_manager.py    # Car spawning and movement
└── scoreboard.py     # Level tracking and game over display

## Requirements

```bash
# Built-in libraries only
from turtle import Turtle, Screen
import time
import random
```

## How to Run

```bash
python main.py
```

## How to Play

1. **Goal**: Get the turtle from the bottom to the top of the screen
2. **Controls**: 
   - Hold **Up Arrow** to move forward
   - Release **Up Arrow** to stop
3. **Avoid**: Colorful cars moving across the screen
4. **Win**: Reach the top to advance to the next level
5. **Lose**: Game ends if you collide with a car

## Game Mechanics

- **Player**: Turtle starts at bottom, moves upward when Up key is held
- **Cars**: Spawn from the right, move left across screen
- **Collision Detection**: Game over if turtle gets within 25 pixels of a car
- **Level System**: Each level increases car speed by 10 pixels
- **Car Spawning**: New car appears every 6 frames (0.6 seconds)

## Features

✅ Progressive difficulty - cars get faster each level  
✅ Hold-to-move controls for smooth gameplay  
✅ Random car colors and positions  
✅ Collision detection  
✅ Level tracking display  
✅ Game over screen  

## Classes Overview

### Player (player.py)
- Turtle-shaped character
- Starts at bottom center
- Moves upward 10 pixels per step
- Resets position after reaching finish line

### CarManager (car_manager.py)
- Spawns random colored cars
- Manages car movement and speed
- Increases difficulty with `level_up()`

### Scoreboard (scoreboard.py)
- Displays current level
- Shows "GAME OVER" on collision
- Updates level counter

## Customization

### Change Difficulty
```python
# In car_manager.py
MOVE_INCREMENT = 5  # Slower difficulty increase
```

### Adjust Car Spawn Rate
```python
# In main.py
if counter % 4 == 0:  # Spawn cars more frequently
```

### Modify Player Speed
```python
# In player.py
MOVE_DISTANCE = 15  # Faster turtle
```

### Add More Colors
```python
# In car_manager.py
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
```

## Controls

| Key | Action |
|-----|--------|
| **Up Arrow (Hold)** | Move forward |
| **Up Arrow (Release)** | Stop moving |
| **Click Screen** | Exit game |

## What I Learned

- **Event handling** - `onkeypress()` and `onkeyrelease()` for hold-to-move controls
- **Game loops** - Using `time.sleep()` and `screen.update()` for animation
- **Collision detection** - Distance-based detection between objects
- **Class inheritance** - Extending Turtle class for custom objects
- **Game progression** - Implementing level systems with increasing difficulty
- **Multi-file projects** - Organizing code across multiple modules

Enjoy crossing the road! 🏁
