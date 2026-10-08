<div align="center">

# ⚔️ Knight Jumpers

**A retro 2D side-scrolling obstacle platformer built with Python and Pygame.**

Navigate through a five-stage dark-fantasy campaign, jump over incoming monsters, survive with three lives, and push your score through increasingly difficult encounters.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2D_Game_Development-0F0F0F?style=for-the-badge)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 🎮 About the Game

**Knight Jumpers** is a small arcade-style 2D game created with **Python** and **Pygame**.

The project focuses on building a complete game loop rather than relying on a game engine. The player controls a knight positioned on the left side of the screen while enemies continuously approach from the right. The main challenge is timing jumps correctly, avoiding collisions, and surviving long enough to progress through all five stages.

The game combines:

* custom gravity and jump physics
* rectangular collision hitboxes
* a life and damage system
* score-based level progression
* level-specific backgrounds and music
* reusable asset-loading modules
* dataclass-based game entities
* start, level-up, and game-over states
* PyInstaller-friendly asset path handling

---

## 🕹️ Gameplay

### Objective

Survive as long as possible by jumping over incoming enemies.

Each enemy that successfully passes off the left side of the screen awards **1 point**. Reaching specific score thresholds advances the player to the next level.

Getting hit removes one life. The player starts every run with **3 lives**.

### Controls

| Key     | Action                                             |
| ------- | -------------------------------------------------- |
| `ENTER` | Start the game / continue after a level transition |
| `SPACE` | Jump                                               |
| `ESC`   | Not assigned in the current build                  |

The player automatically remains on the left side of the screen, so the gameplay is centered around **jump timing rather than horizontal movement**.

---

## ⚔️ Level Progression

The campaign contains five stages with different themes, backgrounds, enemies, and music tracks.

| Level | Name                | Main Enemy | Score to Reach |
| ----: | ------------------- | ---------- | -------------: |
|     1 | **Castle Siege**    | Troll      |           `20` |
|     2 | **Witch Lair**      | Witch      |           `55` |
|     3 | **Skeleton Knight** | Skeleton   |          `100` |
|     4 | **Golems**          | Golem      |          `150` |
|     5 | **Oblivion Gate**   | Moltrex    |          `200` |

The score is cumulative across the run. After a level threshold is reached, the game switches the background and music, changes the active enemy type, and displays a level-up screen before continuing.

At **200 points**, the current implementation reaches the end-of-run screen and resets the run.

---

## ❤️ Lives, Damage & Collision

The game uses a simple three-life system.

When the player's collision rectangle intersects an enemy collision rectangle:

1. One life is removed.
2. A damage sound is played.
3. The enemy is moved back to the right side of the screen.
4. A hit cooldown prevents repeated damage from the same collision.

The hit cooldown lasts **60 frames** at the game's target of **60 FPS**, which corresponds to roughly one second of invulnerability.

### Collision Hitboxes

The visuals and collision areas are intentionally different. Smaller rectangular hitboxes are used to make collision detection more consistent with the character artwork.

**Player hitbox:**

* Offset: `(x + 40, y + 20)`
* Size: `100 × 120`

**Enemy hitbox:**

* Offset: `(x + 20, y + 20)`
* Size: `90 × 110`

This approach avoids relying on the entire sprite rectangle for collision detection.

---

## 🪂 Custom Jump Physics

Knight Jumpers uses a lightweight physics system implemented directly in the game loop.

The player has a vertical velocity (`vy`). Pressing `SPACE` while standing on the ground gives the player an upward velocity, and gravity is then applied every frame.

Conceptually:

```text
vy = vy + gravity
y  = y + vy
```

Current physics constants:

| Setting           |       Value |
| ----------------- | ----------: |
| Gravity           |       `0.7` |
| Jump strength     |        `18` |
| Ground Y position |       `290` |
| Target FPS        |        `60` |
| Resolution        | `640 × 480` |

When the player reaches the ground position, the vertical velocity is reset to `0` and the `on_ground` flag becomes `True`.

---

## 👾 Enemy System

Enemies are represented by a reusable `Enemy` dataclass containing:

* `x` position
* `y` position
* movement `speed`
* enemy `type`

Enemies continuously move from right to left. When an enemy leaves the visible area, it is spawned again beyond the right edge with a randomized speed.

The project also contains separate assets and sound effects for multiple enemy/monster types, including:

* Troll
* Witch
* Skeleton
* Golem variants
* Moltrex
* Bat

The current campaign uses one primary enemy type per level, while the repository contains additional monster assets for experimentation and future gameplay expansion.

---

## 🧠 Game Loop & State Flow

The main game logic is centralized in `game.py`.

The general execution flow is:

```text
Initialize Pygame
      ↓
Load images / backgrounds / sounds / music
      ↓
Create Player and Enemy entities
      ↓
Start Screen
      ↓
┌─────────────────────────────┐
│        Main Game Loop       │
│                             │
│  Handle Events              │
│  Apply Jump Physics         │
│  Apply Gravity              │
│  Move Enemy                 │
│  Check Collisions           │
│  Update Score               │
│  Check Lives                │
│  Check Level Threshold      │
│  Render UI                  │
│                             │
└─────────────────────────────┘
      ↓
Level Up / Game Over
      ↓
Reset or Continue
```

The game is frame-driven and capped using `pygame.time.Clock()` at **60 FPS**.

---

## 🏗️ Project Architecture

The project keeps the core loop in one module while moving entity definitions, configuration, and resource loading into separate modules.

```text
knight-jumpers/
│
├── entities/
│   ├── player.py          # Player dataclass and player state
│   └── enemy.py           # Enemy dataclass and enemy reset logic
│
├── images/                # Sprites, UI graphics and backgrounds
├── pixelizedfont/         # Pixel-style TTF font
├── sfx/                   # Sound effects and background music
│
├── backgrounds.py         # Background loading and scaling
├── colors.py              # Shared RGB color constants
├── game.py                # Main loop, game states, physics and rendering
├── images.py              # Sprite/UI image loading and scaling
├── music.py               # Background music path management
├── settings.py            # Resolution and gameplay constants
├── sounds.py              # Sound effect loading and volume configuration
│
├── .gitignore
├── LICENSE
└── README.md
```

### Module Responsibilities

#### `game.py`

The main application module. It is responsible for:

* initializing Pygame and the mixer
* creating the game window
* loading all resources
* creating player and enemy objects
* processing keyboard and window events
* applying gravity and jump physics
* moving enemies
* performing collision checks
* managing lives and score
* switching levels
* rendering the game UI
* handling start, level-up and game-over screens
* supporting resource paths when packaged with PyInstaller

#### `entities/player.py`

Defines the `Player` entity as a Python `dataclass`.

The model stores the player's position, vertical velocity, lives, ground state, and score.

#### `entities/enemy.py`

Defines the `Enemy` dataclass and provides reset behavior for repositioning an enemy beyond the right side of the screen with a randomized movement speed.

#### `images.py`

Centralizes sprite loading and scaling for player graphics, enemy graphics, hearts, score UI, and the game icon.

#### `backgrounds.py`

Loads menu/end-state backgrounds and scales the level backgrounds to the configured window resolution.

#### `sounds.py`

Loads gameplay sound effects and configures individual volume levels.

#### `music.py`

Maps game states/levels to their background music files.

#### `settings.py`

Contains the core gameplay configuration:

```python
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
GRAVITY = 0.7
JUMP_STRENGTH = 18
```

#### `colors.py`

Stores shared RGB color tuples used by the UI.

---

## 🔊 Audio System

Audio is separated into **background music** and **sound effects**.

### Background Music

Different tracks are associated with:

* Start screen
* Level 1
* Level 2
* Level 3
* Level 4
* Level 5

Music is stopped and replaced whenever the game changes state or level.

### Sound Effects

The project includes effects for actions/events such as:

* jumping
* taking damage
* teleport/transition
* enemy attacks
* game over
* level up
* end-of-run audio assets

All sound files are loaded through `sounds.py`, keeping audio path management outside the main game loop.

---

## 🖼️ Asset Management

The project keeps visual and audio resources outside the Python source code.

### Image Assets

Sprites and UI graphics are stored in `images/`, including the player, enemies, hearts, score icon, menus, level backgrounds, and application icon.

### Font

A pixel-style TrueType font is stored in `pixelizedfont/` and loaded dynamically by the game.

### Audio

Music and sound effects are stored in `sfx/`.

This structure makes it possible to replace or add assets without changing the gameplay logic itself.

---

## 💻 Requirements

The project requires:

* **Python 3.x**
* **Pygame**

There is currently no `requirements.txt` file in the repository, so the dependency can be installed directly with `pip`.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MIhajloS07/knight-jumpers.git
cd knight-jumpers
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Pygame

```bash
pip install pygame
```

### 4. Run the game

```bash
python game.py
```

Make sure the `images/`, `sfx/`, and `pixelizedfont/` directories stay next to the Python source files because the game loads these assets at runtime.

---

## 📦 PyInstaller Support

The game contains explicit support for PyInstaller's bundled-resource path through `sys._MEIPASS`.

For example, on Windows:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed ^
  --add-data "images;images" ^
  --add-data "sfx;sfx" ^
  --add-data "pixelizedfont;pixelizedfont" ^
  game.py
```

The path handling in `game.py` allows the same resource-loading code to work both from the source tree and from a packaged executable.

---

## 🧪 What This Project Demonstrates

Knight Jumpers was built as a practical game-development project and demonstrates several core programming concepts:

* **Game loop design** — continuously processing input, simulation and rendering
* **Real-time physics** — gravity, vertical velocity and grounded state
* **Collision detection** — custom hitboxes using `pygame.Rect`
* **State management** — start, gameplay, level transition and game-over states
* **Data modeling** — Python `dataclass` entities
* **Modularization** — separating game logic from asset/configuration loaders
* **Resource management** — centralized image, music, sound and font loading
* **Randomization** — variable enemy spawn positions and movement speeds
* **UI rendering** — score, lives, level information and transition screens
* **Packaging awareness** — PyInstaller-compatible resource resolution

---

## 🔧 Current Implementation Notes

The repository is an actively developed learning project, so some parts are intentionally simple and provide room for further iteration.

A few implementation details are worth being aware of when working on the current codebase:

* Level 4 currently assigns the enemy key `golem`, while `images.py` defines `golem1` and `golem2`; the asset key should be aligned before the fourth level is considered release-ready.
* The bottom-left level label is initialized from Level 1 and is not updated when the level changes.
* Reaching the Level 5 threshold currently enters the existing end-of-run/game-over screen before resetting the run; the repository also contains a dedicated winner background and `gameWin` sound asset that are prepared for a future victory state.

Potential future improvements include:

* introducing dedicated classes for levels and game states
* expanding enemy behavior beyond horizontal movement
* adding horizontal player movement and attack mechanics
* improving level-specific difficulty balancing
* adding a `requirements.txt` file
* adding automated tests for game-state and collision logic
* separating the main game controller into smaller systems

---

## 📄 License

This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE) for the full license text.

Copyright © 2026 Mihajlo Stoiljković.

---

## 👤 Author

**Mihajlo Stoiljković**

* GitHub: [@MIhajloS07](https://github.com/MIhajloS07)
* Repository: [Knight Jumpers](https://github.com/MIhajloS07/knight-jumpers)

---

<div align="center">

**⚔️ Survive the monsters. Master the jump. Reach the Oblivion Gate. ⚔️**

</div>
