import os

def load_music(base_path: str):
    return {
        "start": os.path.join(base_path, "sfx", "startsound.mp3"),
        "level1": os.path.join(base_path, "sfx", "song.mp3"),
        "level2": os.path.join(base_path, "sfx", "level2main.mp3"),
        "level3": os.path.join(base_path, "sfx", "level3main.mp3"),
        "level4": os.path.join(base_path, "sfx", "level4main.mp3"),
        "level5": os.path.join(base_path, "sfx", "finallevelmusic.mp3"),
    }