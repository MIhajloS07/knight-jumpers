import pygame
import random
import os
import sys

from images import load_images
from backgrounds import load_backgrounds
from music import load_music
from sounds import load_sounds
from entities.player import Player
from entities.enemy import Enemy
from colors import *
from settings import *

# ---------------- BASE PATH ----------------
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

# ---------------- INIT ----------------
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Knight Jumpers")

# ---------------- ASSETS ----------------
images = load_images(base_path)
backgrounds = load_backgrounds(base_path, SCREEN_WIDTH, SCREEN_HEIGHT)
sounds = load_sounds(base_path)
music = load_music(base_path)

pygame.display.set_icon(images["icon"])

# ---------------- FONT ----------------
font_path = os.path.join(base_path, "pixelizedfont", "LcdSolid-VPzB.ttf")
font = pygame.font.Font(font_path, 20)
font_small = pygame.font.Font(font_path, 15)


def draw_center(text, y, color=WHITE_COLOR, fnt=font):
    surf = fnt.render(text, True, color)
    screen.blit(surf, (SCREEN_WIDTH // 2 - surf.get_width() // 2, y))


def play_music(name):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(music[name])
    pygame.mixer.music.play(-1)


# ---------------- PLAYER / ENEMY ----------------
player = Player()

enemy = Enemy(600, 270, random.randint(7, 10), "troll")
moltrex = Enemy(600, 290, random.randint(5, 7), "moltrex")
bat = Enemy(600, 180, random.randint(7, 10), "bat")

current_monster = random.choice([1, 2])

# ---------------- GAME STATE ----------------
points = 0
level = 1
max_lives = 3
hit_cooldown = 0

level_names = [
    "Level 1 - Castle Siege",
    "Level 2 - Witch Lair",
    "Level 3 - Skeleton Knight",
    "Level 4 - Golems",
    "Level 5 - Oblivion Gate"
]

current_enemy = "troll"
current_background = backgrounds["level1"]
currentLevel_text = level_names[0]


# ---------------- SCREENS ----------------
def start_screen():
    play_music("start")

    waiting = True
    while waiting:
        screen.blit(backgrounds["start"], (0, 0))
        draw_center("KNIGHT JUMPERS", 180, ORANGERED_COLOR)
        draw_center("Press ENTER to start", 260)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                sounds["teleport"].play()
                play_music("level1")
                waiting = False


def game_over_screen():
    pygame.mixer.music.stop()
    sounds["gameOver"].play()

    waiting = True
    while waiting:
        screen.blit(backgrounds["gameover"], (0, 0))
        draw_center("GAME OVER", 180, RED_COLOR)
        draw_center(f"Points: {points}", 250)
        draw_center("Press ENTER to restart", 320)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                sounds["gameOver"].stop()
                waiting = False


def level_up_screen():
    pygame.mixer.music.stop()
    sounds["levelup"].play()

    waiting = True
    while waiting:
        screen.blit(current_background, (0, 0))
        draw_center("LEVEL UP", 180, GREEN_COLOR)
        draw_center("Press ENTER", 260)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                sounds["levelup"].stop()
                sounds["teleport"].play()
                waiting = False


def reset_enemy():
    enemy.x = SCREEN_WIDTH + random.randint(80, 200)
    enemy.speed = random.randint(7, 12)


# ---------------- START ----------------
start_screen()

running = True
while running:

    screen.blit(current_background, (0, 0))

    if hit_cooldown > 0:
        hit_cooldown -= 1

    # ---------------- EVENTS ----------------
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and player.on_ground:
                player.vy = -JUMP_STRENGTH
                player.on_ground = False
                sounds["jump"].play()

    # ---------------- GRAVITY ----------------
    player.vy += GRAVITY
    player.y += player.vy

    if player.y >= 290:
        player.y = 290
        player.vy = 0
        player.on_ground = True

    # ---------------- ENEMY ----------------
    enemy.x -= enemy.speed

    if enemy.x < -120:
        enemy.x = SCREEN_WIDTH + 100
        enemy.speed = random.randint(7, 12)
        points += 1

    screen.blit(images[current_enemy], (enemy.x, enemy.y))
    screen.blit(images["player"], (player.x, player.y))
    
    enemy_rect = pygame.Rect(enemy.x + 20, enemy.y + 20, 90, 110)
    player_rect = pygame.Rect(player.x + 40, player.y + 20, 100, 120)

    # ---------------- EXTRA HIT FIX ----------------
    if abs(enemy.x - player.x) < 15 and player_rect.colliderect(enemy_rect):
        if hit_cooldown == 0:
            player.lives -= 1
            hit_cooldown = 60
            sounds["damage"].play()
            reset_enemy()

    # ---------------- NORMAL COLLISION ----------------
    if hit_cooldown == 0 and player_rect.colliderect(enemy_rect):
        player.lives -= 1
        hit_cooldown = 60
        sounds["damage"].play()
        reset_enemy()

    # ---------------- GAME OVER ----------------
    if player.lives <= 0:
        game_over_screen()

        player.lives = 3
        points = 0
        level = 1
        current_enemy = "troll"
        current_background = backgrounds["level1"]
        play_music("level1")

    # ---------------- LEVELS ----------------
    if level == 1 and points >= 20:
        level = 2
        current_enemy = "witch"
        current_background = backgrounds["level2"]
        level_up_screen()
        play_music("level2")

    elif level == 2 and points >= 55:
        level = 3
        current_enemy = "skeleton"
        current_background = backgrounds["level3"]
        level_up_screen()
        play_music("level3")

    elif level == 3 and points >= 100:
        level = 4
        current_enemy = "golem"
        current_background = backgrounds["level4"]
        level_up_screen()
        play_music("level4")

    elif level == 4 and points >= 150:
        level = 5
        current_enemy = "moltrex"
        current_background = backgrounds["level5"]
        level_up_screen()
        play_music("level5")

    elif level == 5 and points >= 200:
        game_over_screen()

        player.lives = 3
        points = 0
        level = 1
        current_enemy = "troll"
        current_background = backgrounds["level1"]
        play_music("level1")

    # ---------------- UI ----------------
    screen.blit(images["points"], (500, 20))
    draw_center(str(points), 25)

    for i in range(max_lives):
        img = images["full_heart"] if i < player.lives else images["empty_heart"]
        screen.blit(img, (20 + i * 50, 20))

    lvl_text = font_small.render(currentLevel_text, True, WHITE_COLOR)
    screen.blit(lvl_text, (20, 450))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()