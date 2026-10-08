import pygame
import os

def load_backgrounds(base_path: str, screen_width: int, screen_height: int):
    return {
        "start": pygame.image.load(os.path.join(base_path, "images", "startgame.jpg")),
        "gameover": pygame.image.load(os.path.join(base_path, "images", "endgame.png")),
        "win": pygame.image.load(os.path.join(base_path, "images", "winnerbackground.png")),

        "level1": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "JEMA GER 1449-05.jpg")),
            (screen_width, screen_height)
        ),
        "level2": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "level2scene.jpg")),
            (screen_width, screen_height)
        ),
        "level3": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "level3scene.jpg")),
            (screen_width, screen_height)
        ),
        "level4": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "level4scene.png")),
            (screen_width, screen_height)
        ),
        "level5": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "level5scene.png")),
            (screen_width, screen_height)
        ),
    }