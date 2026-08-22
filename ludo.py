import pygame
import random
import sys

pygame.init()

# -----------------------------
# WINDOW
# -----------------------------
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Ludo Game")

clock = pygame.time.Clock()

# -----------------------------
# COLORS
# -----------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 180, 80)
BLUE = (60, 120, 220)
YELLOW = (240, 200, 50)
GREY = (220, 220, 220)

# -----------------------------
# FONTS
# -----------------------------
font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 40)

# -----------------------------
# BOARD SETTINGS
# -----------------------------
BOARD_X = 100
BOARD_Y = 100
CELL_SIZE = 40

# Simple 15x15 Ludo board
BOARD_SIZE = 15

# -----------------------------
# PLAYER DATA
# -----------------------------
players = {
    "RED": {
        "color": RED,
        "position": 0,
        "tokens": [-1, -1, -1, -1]
    },
    "GREEN": {
        "color": GREEN,
        "position": 0,
        "tokens": [-1, -1, -1, -1]
    }
}

player_names = ["RED", "GREEN"]
current_player = 0

dice_value = 1
message = "RED player's turn"

# -----------------------------
# TOKEN HOME POSITIONS
# -----------------------------
home_positions = {
    "RED": [
        (3, 3),
        (5, 3),
        (3, 5),
        (5, 5)
    ],

    "GREEN": [
        (9, 3),
        (11, 3),
        (9, 5),
        (11, 5)
    ]
}

# -----------------------------
# TRACK
# -----------------------------
track = []

for x in range(1, 14):
    track.append((x, 7))

for y in range(6, 1, -1):
    track.append((13, y))

for x in range(12, 0, -1):
    track.append((x, 2))

for y in range(3, 7):
    track.append((1, y))

# Remove duplicate positions
track = list(dict.fromkeys(track))

# -----------------------------
# DRAW BOARD
# -----------------------------
def draw_board():

    screen.fill(WHITE)

    # Board background
    pygame.draw.rect(
        screen,
        GREY,
        (
            BOARD_X,
            BOARD_Y,
            BOARD_SIZE * CELL_SIZE,
            BOARD_SIZE * CELL_SIZE
        )
    )

    # Grid
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):

            rect = pygame.Rect(
                BOARD_X + col * CELL_SIZE,
                BOARD_Y + row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(
                screen,
                BLACK,
                rect,
                1
            )

    # Red home
    pygame.draw.rect(
        screen,
        RED,
        (
            BOARD_X + CELL_SIZE,
            BOARD_Y + CELL_SIZE,
            CELL_SIZE * 5,
            CELL_SIZE * 5
        ),
        4
    )

    # Green home
    pygame.draw.rect(
        screen,
        GREEN,
        (
            BOARD_X + CELL_SIZE * 9,
            BOARD_Y + CELL_SIZE,
            CELL_SIZE * 5,
            CELL_SIZE * 5
        ),
        4
    )

    # Center
    pygame.draw.rect(
        screen,
        YELLOW,
        (
            BOARD_X + CELL_SIZE * 6,
            BOARD_Y + CELL_SIZE * 6,
            CELL_SIZE * 3,
            CELL_SIZE * 3
        )
    )

    # Track
    for x, y in track:

        rect = pygame.Rect(
            BOARD_X + x * CELL_SIZE,
            BOARD_Y + y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )

        pygame.draw.rect(
            screen,
            WHITE,
            rect
        )

        pygame.draw.rect(
            screen,
            BLACK,
            rect,
            1
        )


# -----------------------------
# DRAW TOKENS
# -----------------------------
def draw_tokens():

    for player in player_names:

        color = players[player]["color"]

        for i, position in enumerate(players[player]["tokens"]):

            # Token is at home
            if position == -1:

                grid_x, grid_y = home_positions[player][i]

            else:

                if position < len(track):
                    grid_x, grid_y = track[position]
                else:
                    grid_x, grid_y = track[-1]

            x = BOARD_X + grid_x * CELL_SIZE + CELL_SIZE // 2
            y = BOARD_Y + grid_y * CELL_SIZE + CELL_SIZE // 2

            pygame.draw.circle(
                screen,
                color,
                (x, y),
                14
            )

            pygame.draw.circle(
                screen,
                BLACK,
                (x, y),
                14,
                2
            )


# -----------------------------
# DRAW TEXT
# -----------------------------
def draw_text():

    title = big_font.render(
        "PYTHON LUDO",
        True,
        BLACK
    )

    screen.blit(
        title,
        (280, 20)
    )

    turn_text = font.render(
        message,
        True,
        BLACK
    )

    screen.blit(
        turn_text,
        (250, 720)
    )

    dice_text = font.render(
        "Dice: " + str(dice_value),
        True,
        BLACK
    )

    screen.blit(
        dice_text,
        (350, 760)
    )


# -----------------------------
# ROLL DICE
# -----------------------------
def roll_dice():

    global dice_value
    global current_player
    global message

    dice_value = random.randint(1, 6)

    player = player_names[current_player]

    message = f"{player} rolled {dice_value}"

    # Move first available token
    move_token(player, dice_value)

    # Change player
    if dice_value != 6:

        current_player = 1 - current_player

        next_player = player_names[current_player]

        message = f"{next_player} player's turn"


# -----------------------------
# MOVE TOKEN
# -----------------------------
def move_token(player, steps):

    tokens = players[player]["tokens"]

    # Find a token already on board
    for i in range(len(tokens)):

        if tokens[i] != -1:

            new_position = tokens[i] + steps

            if new_position < len(track):

                tokens[i] = new_position

                check_winner(player)

                return

    # If dice is 6, bring token out
    if steps == 6:

        for i in range(len(tokens)):

            if tokens[i] == -1:

                tokens[i] = 0

                check_winner(player)

                return


# -----------------------------
# CHECK WINNER
# -----------------------------
def check_winner(player):

    tokens = players[player]["tokens"]

    # Simple winning condition
    if all(position == len(track) - 1 for position in tokens):

        global message

        message = f"{player} WINS!"

        print(message)


# -----------------------------
# RESET GAME
# -----------------------------
def reset_game():

    global current_player
    global dice_value
    global message

    for player in player_names:

        players[player]["tokens"] = [
            -1,
            -1,
            -1,
            -1
        ]

    current_player = 0
    dice_value = 1

    message = "RED player's turn"


# -----------------------------
# MAIN GAME LOOP
# -----------------------------
running = True

while running:

    for event in pygame.event.get():

        # Close game
        if event.type == pygame.QUIT:

            running = False

        # Keyboard
        if event.type == pygame.KEYDOWN:

            # Press SPACE to roll dice
            if event.key == pygame.K_SPACE:

                roll_dice()

            # Press R to restart
            if event.key == pygame.K_r:

                reset_game()

    draw_board()

    draw_tokens()

    draw_text()

    pygame.display.update()

    clock.tick(60)


pygame.quit()
sys.exit()