import pygame
import board
import setup_board

pygame.init()
pygame.display.set_caption("Tom's Chess Bot")
icon = pygame.image.load('assets/misc/icon.png')
pygame.display.set_icon(icon)

# Starting Chess Positon
STARTING_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

# Board Colours
LIGHT_SQUARES = (234,234,210)
DARK_SQUARES = (75,115,153)

# pygame config
SCREEN = pygame.display.set_mode((800,800))

PIECES_ARR = []
setup_board.setup_board(STARTING_FEN, PIECES_ARR)
print(PIECES_ARR)

# game loop
run = True
move_piece = False
clock = pygame.time.Clock()

while run:
	# event handler
    for event in pygame.event.get():		
		# quit game
        if event.type == pygame.QUIT:
            run = False
        #place piece
        if event.type == pygame.MOUSEBUTTONUP and move_piece:
            GOAL_SQUARE = board.get_index(mx,my)
            board.perform_move(MOVING_PIECE, PIECES_ARR, START_SQUARE, GOAL_SQUARE)
            move_piece = False
            
    #draw the board
    board.draw(SCREEN, LIGHT_SQUARES, DARK_SQUARES)

	# get the positions of the mouse
    mx,my = pygame.mouse.get_pos()
    for i in range(len(PIECES_ARR)):
        if PIECES_ARR[i] != " ":
            if PIECES_ARR[i].draw(SCREEN) and not move_piece:
                START_SQUARE = board.get_index(mx,my)
                MOVING_PIECE = PIECES_ARR[i]
                PIECES_ARR[i] = " "
                move_piece = True

    if move_piece:
        MOVING_PIECE.set_coordinates(mx-50, my-50)
        MOVING_PIECE.draw(SCREEN)
            
    pygame.display.update()
    
    # 120 fps
    clock.tick(120)

pygame.quit()
