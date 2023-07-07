import pygame

def draw(SCREEN, LIGHT_SQUARES, DARK_SQUARES):

    SCREEN.fill(LIGHT_SQUARES)

    for y in range(8):
        if y % 2 == 0: offset = 100
        else: offset = 0
        for x in range(4):
            pygame.draw.rect(SCREEN, DARK_SQUARES, pygame.Rect((100*(x*2))+offset,(y*100), 100, 100))

def get_index(mx,my):
	x_coord = int(mx / 100)
	y_coord = int(my / 100)
	coordinates_x = [0,1,2,3,4,5,6,7]
	coordinates_y = [0,8,16,24,32,40,48,56]
	return coordinates_x[x_coord] + coordinates_y[y_coord]

def perform_move(MOVING_PIECE, PIECES_ARR, START_INDEX, GOAL_INDEX):

    #sounds
    move_sound = pygame.mixer.Sound("assets/audio/move.wav")
    capture_sound = pygame.mixer.Sound("assets/audio/capture.wav")

    if PIECES_ARR[GOAL_INDEX] == " ":
        PIECES_ARR[GOAL_INDEX] = MOVING_PIECE
        move_sound.play()

    elif PIECES_ARR[GOAL_INDEX] != " " and MOVING_PIECE.get_colour() != PIECES_ARR[GOAL_INDEX].get_colour():
        PIECES_ARR[GOAL_INDEX] = MOVING_PIECE
        capture_sound.play()

    else:
        invalid_move(MOVING_PIECE, PIECES_ARR, START_INDEX)

def invalid_move(MOVING_PIECE, PIECES_ARR, START_INDEX):
    PIECES_ARR[START_INDEX] = MOVING_PIECE
    MOVING_PIECE.move_piece(START_INDEX)

