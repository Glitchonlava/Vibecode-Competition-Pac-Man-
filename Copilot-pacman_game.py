import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 560, 620
ROWS, COLS = 31, 28
TILE_SIZE = 20

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Style Game")

# Clock
clock = pygame.time.Clock()

# Maze layout (1 = wall, 0 = path)
maze = [
    [1]*COLS,
] + [
    [1] + [0]*(COLS-2) + [1] for _ in range(ROWS-2)
] + [
    [1]*COLS,
]

# Player setup
player_x, player_y = TILE_SIZE*14, TILE_SIZE*23
player_speed = TILE_SIZE

def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw_player(x, y):
    pygame.draw.circle(screen, YELLOW, (x+TILE_SIZE//2, y+TILE_SIZE//2), TILE_SIZE//2)

def can_move(x, y):
    col, row = x // TILE_SIZE, y // TILE_SIZE
    return maze[row][col] == 0

# Game loop
while True:
    screen.fill(BLACK)
    draw_maze()
    draw_player(player_x, player_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and can_move(player_x - player_speed, player_y):
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and can_move(player_x + player_speed, player_y):
        player_x += player_speed
    if keys[pygame.K_UP] and can_move(player_x, player_y - player_speed):
        player_y -= player_speed
    if keys[pygame.K_DOWN] and can_move(player_x, player_y + player_speed):
        player_y += player_speed

    pygame.display.update()
    clock.tick(10)
