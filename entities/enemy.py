from dataclasses import dataclass
import random

@dataclass
class Enemy:
    x: int
    y: int
    speed: int
    type: str

    def reset(self, screen_width: int):
        self.x = screen_width + random.randint(50, 150)
        self.speed = random.randint(6, 12)