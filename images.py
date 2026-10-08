import pygame
import os

def load_images(base_path: str):
    images = {
        # UI
        "full_heart": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "fullheart.png")), (30, 30)
        ),
        "empty_heart": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "emptyheart.png")), (30, 30)
        ),
        "points": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "Points.png")), (45, 45)
        ),

        # player
        "player": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "knight (2).png")), (170, 140)
        ),

        # enemies
        "troll": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "troll.png")), (130, 170)
        ),
        "witch": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "witch.png")), (130, 170)
        ),
        "skeleton": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "skeleton.png")), (130, 150)
        ),

        # golems
        "golem1": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "golemone.png")), (140, 170)
        ),
        "golem2": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "golemtwo.gif")), (130, 150)
        ),

        # monsters
        "moltrex": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "Moltrex.png")), (125, 150)
        ),
        "bat": pygame.transform.scale(
            pygame.image.load(os.path.join(base_path, "images", "bat.png")), (45, 55)
        ),

        # misc
        "icon": pygame.image.load(os.path.join(base_path, "images", "icon.png")),
    }

    return images