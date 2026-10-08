import pygame
import os

def load_sounds(base_path: str):
    sounds = {
        "jump": pygame.mixer.Sound(os.path.join(base_path, "sfx", "retrojump.mp3")),
        "damage": pygame.mixer.Sound(os.path.join(base_path, "sfx", "hurt.mp3")),
        "teleport": pygame.mixer.Sound(os.path.join(base_path, "sfx", "teleport.mp3")),
        "laugh": pygame.mixer.Sound(os.path.join(base_path, "sfx", "laugh.mp3")),
        "trollAttack": pygame.mixer.Sound(os.path.join(base_path, "sfx", "troll_atack.mp3")),
        "skeletonAttack": pygame.mixer.Sound(os.path.join(base_path, "sfx", "swordattacksound.mp3")),
        "witchAttack": pygame.mixer.Sound(os.path.join(base_path, "sfx", "witch_attack.mp3")),
        "golemAttack": pygame.mixer.Sound(os.path.join(base_path, "sfx", "golemattacksound.mp3")),
        "moltrexAttack": pygame.mixer.Sound(os.path.join(base_path, "sfx", "moltrex_attack.mp3")),
        "batAttack": pygame.mixer.Sound(os.path.join(base_path, "sfx", "bat_attack.mp3")),
        "gameOver": pygame.mixer.Sound(os.path.join(base_path, "sfx", "gameover.mp3")),
        "gameWin": pygame.mixer.Sound(os.path.join(base_path, "sfx", "gamewin.mp3")),
        "levelup": pygame.mixer.Sound(os.path.join(base_path, "sfx", "level-up.mp3")),
    }

    # volume
    sounds["jump"].set_volume(0.1)
    sounds["damage"].set_volume(0.15)
    sounds["teleport"].set_volume(0.18)
    sounds["laugh"].set_volume(0.25)

    for key in ["trollAttack", "skeletonAttack", "witchAttack",
                "golemAttack", "moltrexAttack", "batAttack",
                "gameOver", "gameWin", "levelup"]:
        sounds[key].set_volume(0.1)

    return sounds