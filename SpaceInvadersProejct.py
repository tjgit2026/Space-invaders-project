
# ROCKET VS. SPACE INVADERS GAME

# Import necessary libraries
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rocket vs. Space Invaders")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Create the player (rocket)
player_x = 375
player_y = 500
player_width = 50
player_height = 50
player_speed = 5

# Player movement variables
move_left = False
move_right = False
move_up = False
move_down = False

# Create two lists for seven enemies
enemy_x = []
enemy_y = []

for i in range(7):
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 40))
    enemy_y.append(random.randint(20, 300))

# Enemy size
enemy_width = 40
enemy_height = 40

# Score
score = 0

# Create collision detection function
def isCollision(player_x, player_y, enemy_x, enemy_y):

    distance = math.sqrt(
        (player_x - enemy_x) ** 2 +
        (player_y - enemy_y) ** 2
    )

    if distance < 40:
        return True
    else:
        return False

# Game loop
running = True
clock = pygame.time.Clock()

while running:

    screen.fill(BLACK)

    # Check events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN: Start moving
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                move_left = True

            if event.key == pygame.K_RIGHT:
                move_right = True

            if event.key == pygame.K_UP:
                move_up = True

            if event.key == pygame.K_DOWN:
                move_down = True

        # KEYUP: Stop moving
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                move_left = False

            if event.key == pygame.K_RIGHT:
                move_right = False

            if event.key == pygame.K_UP:
                move_up = False

            if event.key == pygame.K_DOWN:
                move_down = False

    # Move the player
    if move_left:
        player_x -= player_speed

    if move_right:
        player_x += player_speed

    if move_up:
        player_y -= player_speed

    if move_down:
        player_y += player_speed

    # Keep the player inside the window
    player_x = max(0, min(player_x, SCREEN_WIDTH - player_width))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - player_height))

    # Draw the player (rocket)
    pygame.draw.polygon(
        screen,
        GREEN,
        [
            (player_x + 25, player_y),
            (player_x, player_y + 50),
            (player_x + 50, player_y + 50)
        ]
    )

    # Draw enemies and check collisions
    for i in range(7):

        # Draw enemy
        pygame.draw.circle(
            screen,
            RED,
            (enemy_x[i] + 20, enemy_y[i] + 20),
            20
        )

        # Check collision
        if isCollision(
            player_x + 25,
            player_y + 25,
            enemy_x[i] + 20,
            enemy_y[i] + 20
        ):

            # Increase score
            score += 1

            # Move enemy to a new random position
            enemy_x[i] = random.randint(0, SCREEN_WIDTH - enemy_width)
            enemy_y[i] = random.randint(20, SCREEN_HEIGHT - enemy_height)

    # Display score
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

    # Control game speed
    clock.tick(60)

# Close Pygame
pygame.quit()
