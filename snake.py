import pygame
import random
import sys

# Initialize pygame
pygame.init()

# -----------------------------
# GAME SETTINGS
# -----------------------------
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Snake Game")

clock = pygame.time.Clock()

# -----------------------------
# COLORS
# -----------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
GRAY = (40, 40, 40)

# -----------------------------
# FONT
# -----------------------------
font = pygame.font.SysFont("Arial", 25)
game_over_font = pygame.font.SysFont("Arial", 50)


# -----------------------------
# DRAW SNAKE
# -----------------------------
def draw_snake(snake):

    for block in snake:

        pygame.draw.rect(
            screen,
            GREEN,
            (
                block[0],
                block[1],
                BLOCK_SIZE,
                BLOCK_SIZE
            )
        )


# -----------------------------
# CREATE FOOD
# -----------------------------
def create_food():

    x = random.randrange(
        0,
        WIDTH - BLOCK_SIZE,
        BLOCK_SIZE
    )

    y = random.randrange(
        0,
        HEIGHT - BLOCK_SIZE,
        BLOCK_SIZE
    )

    return [x, y]


# -----------------------------
# DISPLAY SCORE
# -----------------------------
def display_score(score):

    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (10, 10)
    )


# -----------------------------
# GAME OVER SCREEN
# -----------------------------
def game_over(score):

    screen.fill(BLACK)

    text = game_over_font.render(
        "GAME OVER",
        True,
        RED
    )

    screen.blit(
        text,
        (180, 130)
    )

    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (250, 200)
    )

    restart_text = font.render(
        "Press R to Restart or Q to Quit",
        True,
        WHITE
    )

    screen.blit(
        restart_text,
        (145, 250)
    )

    pygame.display.update()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    return

                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


# -----------------------------
# MAIN GAME
# -----------------------------
def game():

    snake = [
        [300, 200],
        [280, 200],
        [260, 200]
    ]

    direction = "RIGHT"

    food = create_food()

    score = 0

    running = True

    while running:

        # -------------------------
        # EVENTS
        # -------------------------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if direction != "DOWN":
                        direction = "UP"

                elif event.key == pygame.K_DOWN:
                    if direction != "UP":
                        direction = "DOWN"

                elif event.key == pygame.K_LEFT:
                    if direction != "RIGHT":
                        direction = "LEFT"

                elif event.key == pygame.K_RIGHT:
                    if direction != "LEFT":
                        direction = "RIGHT"

        # -------------------------
        # MOVE SNAKE
        # -------------------------
        head = snake[0].copy()

        if direction == "UP":
            head[1] -= BLOCK_SIZE

        elif direction == "DOWN":
            head[1] += BLOCK_SIZE

        elif direction == "LEFT":
            head[0] -= BLOCK_SIZE

        elif direction == "RIGHT":
            head[0] += BLOCK_SIZE

        snake.insert(0, head)

        # -------------------------
        # CHECK FOOD
        # -------------------------
        if head == food:

            score += 1

            food = create_food()

            # Make sure food isn't inside snake
            while food in snake:
                food = create_food()

        else:

            snake.pop()

        # -------------------------
        # WALL COLLISION
        # -------------------------
        if (
            head[0] < 0
            or head[0] >= WIDTH
            or head[1] < 0
            or head[1] >= HEIGHT
        ):
            running = False

        # -------------------------
        # SELF COLLISION
        # -------------------------
        if head in snake[1:]:
            running = False

        # -------------------------
        # DRAW GAME
        # -------------------------
        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(
            screen,
            RED,
            (
                food[0],
                food[1],
                BLOCK_SIZE,
                BLOCK_SIZE
            )
        )

        # Draw snake
        draw_snake(snake)

        # Draw score
        display_score(score)

        pygame.display.update()

        # Game speed
        clock.tick(10)

    # Game over
    game_over(score)


# -----------------------------
# START GAME
# -----------------------------
while True:
    game()