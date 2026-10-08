from dataclasses import dataclass

@dataclass
class Player:
    x: int = 100
    y: int = 250
    vy: float = 0
    lives: int = 3
    on_ground: bool = True
    points: int = 0