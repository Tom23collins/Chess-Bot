# Imports
import pygame
import board
import setup_board

# Game Setup
pygame.init()
pygame.display.set_caption("Tom's Chess Bot")
pygame.display.set_icon(pygame.image.load('assets/misc/icon.png')) # Custom Icon in top corner
STARTING_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
LIGHT_SQUARES = (234,234,210)
DARK_SQUARES = (75,115,153)
SCREEN = pygame.display.set_mode((800,800)) # create window
PIECES_ARR = []
setup_board.setup_board(STARTING_FEN, PIECES_ARR)

# game loop
run = True
performing_move = False
clock = pygame.time.Clock()

while run:
	# event handler
    for event in pygame.event.get():		
        if event.type == pygame.QUIT:
            run = False # quit game
        
        if event.type == pygame.MOUSEBUTTONUP and performing_move:
            board.perform_move(MOVING_PIECE, PIECES_ARR, START_SQUARE, board.get_index(mx,my)) #place piece
            performing_move = False
            
    board.draw(SCREEN, LIGHT_SQUARES, DARK_SQUARES)
    mx,my = pygame.mouse.get_pos() 

    # Draw pieces onto screen
    for i in range(len(PIECES_ARR)):
        if PIECES_ARR[i] != " ":
            if PIECES_ARR[i].draw(SCREEN) and not performing_move:
                START_SQUARE = board.get_index(mx,my)
                MOVING_PIECE = PIECES_ARR[i]
                PIECES_ARR[i] = " "
                performing_move = True

    # Dragging Piece across board
    if performing_move:
        MOVING_PIECE.set_coordinates(mx-50, my-50)
        MOVING_PIECE.draw(SCREEN)
            
    pygame.display.update()
    clock.tick(120) # 120 fps

pygame.quit()
