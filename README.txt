Knight Jumpers - README
Description

Knight Jumpers is a 2D side-scrolling action game developed using Python and Pygame.
The player controls a knight who must jump over or avoid various enemies while progressing through multiple levels.

Features

Five exciting levels with unique backgrounds and enemies.

Multiple enemy types: Troll, Witch, Skeleton, Golems, Moltrex, and Bat.

Collect points by surviving enemy attacks and advancing through levels.

Player health system with visual heart indicators.

Sounds for actions, attacks, and background music for each level.

Game over and level-up screens with interactive controls.

Controls

SPACE → Jump

ENTER → Start game / Proceed to next level / Restart game

Installation

Make sure Python 3.12+ is installed.

Install required dependencies using:

pip install pygame


Run the game:

python game.py


Or use the executable in the dist folder if you built it using PyInstaller.

Building Executable

To create a standalone executable for Windows:

pyinstaller --onefile --add-data "pixelizedfont;pixelizedfont" --add-data "images;images" --add-data "sfx;sfx" game.py

Folder Structure
minigame/
│
├── game.py
├── pixelizedfont/         # Contains fonts used in the game
├── images/                # Game graphics and sprites
├── sfx/                   # Sound effects and music
└── README.txt             # This file

Notes

Ensure all asset folders (pixelizedfont, images, sfx) are included when running the executable.

The game is designed for 640x480 resolution. Full-screen scaling is not supported.