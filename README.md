# ⚔️ Knight Jumpers

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

A 2D arcade-style side-scrolling platformer built in Python using Pygame. Navigate through a 5-level campaign—from the Castle Siege to the Oblivion Gate—featuring custom jump physics, scaling difficulty, unique monster encounters, and a structured audio/asset system.

---

## 🎮 Gameplay & Features

- **5-Level Campaign Progression:**
  1. *Castle Siege* — Troll
  2. *Witch Lair* — Witch
  3. *Skeleton Knight* — Skeleton
  4. *Golems* — Golem
  5. *Oblivion Gate* — Moltrex
- **Custom Physics Engine:** Gravity-based vertical acceleration with collision hitboxes and cooldown buffers.
- **Audio State System:** Dynamic background music tracks per level and dedicated sound effects for jumping, taking damage, leveling up, and game-over states.
- **Modular Code Architecture:** Clean separation of concerns with standalone asset loaders, data models, and configuration modules.
- **Standalone Compatibility:** Configured with `sys._MEIPASS` dynamic path handling for seamless executable bundling via PyInstaller.

---

## 🛠️ Project Architecture

```text
knight-jumpers/
├── entities/
│   ├── enemy.py         # Enemy dataclass model & positioning logic
│   └── player.py        # Player dataclass model & state properties
├── images/              # Game sprites & UI assets
├── pixelizedfont/       # Custom pixel font typography
├── sfx/                 # Sound effects & background music files
├── backgrounds.py       # Background image loaders & resolution scalers
├── colors.py            # RGB color tuple constants
├── images.py            # Texture & sprite asset management
├── main.py              # Core game loop, rendering pipelines & state machine
├── music.py             # Background music path mappings
├── settings.py          # Screen resolution, FPS limit, & physics constants
└── sounds.py            # SFX loaders & mixer volume control
