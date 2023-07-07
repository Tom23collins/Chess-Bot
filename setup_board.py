import pygame
import pieces
import fen_to_board

def create_piece(image, x, y):
    colour = 0
    if image[0] == "b":
        colour = 1
    image = pygame.image.load(f"assets/pieces/{image}.png")
    image = pygame.transform.smoothscale(image, (100, 100))
    
    return pieces.piece(x,y,image, colour)

def setup_board(fen, PIECES_ARR):
    for rank in range(8):
        for square in range(8):
            if fen_to_board.convert(fen)[rank][square] == ' ':
                PIECES_ARR.append(" ")
            else:
                PIECES_ARR.append(create_piece(fen_to_board.convert(fen)[rank][square], square*100, rank*100))
