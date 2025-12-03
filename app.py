import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_width, player_height = 80, 15
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 30
player_speed = 7

# Ball settings
ball_radius = 10
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = -ball_radius
ball_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Ball movement
    ball_y += ball_speed
    if ball_y > HEIGHT:
        ball_y = -ball_radius
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)

    # Collision detection
    if (player_y < ball_y + ball_radius < player_y + player_height and
        player_x < ball_x < player_x + player_width):
        score += 1
        ball_y = -ball_radius
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()