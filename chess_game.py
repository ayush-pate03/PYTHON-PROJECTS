import pygame
import chess
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 640
HEIGHT = 640
SQUARE_SIZE = WIDTH // 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Chess Game")

# Colors
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
HIGHLIGHT = (186, 202, 68)

# Font for chess pieces
font = pygame.font.SysFont("Arial", 50)

# Chess board
board = chess.Board()

# Selected square
selected_square = None


def draw_board():
    """Draw the chess board."""
    for row in range(8):
        for col in range(8):

            color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE

            # Highlight selected square
            square = chess.square(col, 7 - row)

            if square == selected_square:
                color = HIGHLIGHT

            pygame.draw.rect(
                screen,
                color,
                (col * SQUARE_SIZE,
                 row * SQUARE_SIZE,
                 SQUARE_SIZE,
                 SQUARE_SIZE)
            )


def draw_pieces():
    """Draw chess pieces."""

    piece_symbols = {
        "P": "♙",
        "N": "♘",
        "B": "♗",
        "R": "♖",
        "Q": "♕",
        "K": "♔",

        "p": "♟",
        "n": "♞",
        "b": "♝",
        "r": "♜",
        "q": "♛",
        "k": "♚"
    }

    for square in chess.SQUARES:

        piece = board.piece_at(square)

        if piece is not None:

            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)

            symbol = piece_symbols[piece.symbol()]

            text = font.render(symbol, True, (0, 0, 0))

            x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            y = row * SQUARE_SIZE + SQUARE_SIZE // 2

            text_rect = text.get_rect(center=(x, y))

            screen.blit(text, text_rect)


def get_square_from_mouse(pos):
    """Convert mouse position to chess square."""

    x, y = pos

    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE

    return chess.square(col, 7 - row)


def make_move(from_square, to_square):

    move = chess.Move(from_square, to_square)

    if move in board.legal_moves:

        board.push(move)

        return True

    return False


# Main game loop
running = True

while running:

    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False

        # Mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:

            square = get_square_from_mouse(event.pos)

            # Select a piece
            if selected_square is None:

                piece = board.piece_at(square)

                if piece is not None:

                    # Only allow current player's pieces
                    if piece.color == board.turn:

                        selected_square = square

            # Move selected piece
            else:

                if make_move(selected_square, square):

                    selected_square = None

                else:

                    # Select another piece
                    piece = board.piece_at(square)

                    if piece is not None and piece.color == board.turn:
                        selected_square = square
                    else:
                        selected_square = None

    # Draw board
    draw_board()

    # Draw pieces
    draw_pieces()

    pygame.display.flip()


pygame.quit()
sys.exit()