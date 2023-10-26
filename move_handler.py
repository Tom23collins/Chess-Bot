def pawn_moves(current_x,current_y, colour):

    def check_square(x,y):
        return True

    # if pawn is on its starting square then it can move two spaces
    if current_y == 1:
        two_squares = True

    # if there is an enemy diagonal then it can take
    if check_square(current_x + 1, current_y + 1):
        take_right = True

    # if there is an enemy diagonal then it can take
    if check_square(current_x - 1, current_y + 1):
        take_left = True

    