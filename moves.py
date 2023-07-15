def is_rook_move_valid(start_index, end_index):

    # check if both moves are on the same column
    if start_index % 8 == end_index % 8: 

        # check if there are no pieces blocking the move
        if start_index >= end_index:
            for i in range((start_index - end_index) // 8):
                square = start_index - (8 * i)
                if not empty_square(square):
                    return False
        else:
            for i in range((end_index - start_index) // 8):
                square = start_index + (8 * i)
                if not empty_square(square):
                    return False

    # check if both moves are on the same rank
    elif start_index - (start_index % 8) == end_index - (end_index % 8):  

        # check if there are no pieces blocking the move
        if start_index >= end_index:
            for i in range(start_index - end_index):
                square = start_index - i
                if not empty_square(square):
                    return False
        else:
            for i in range(end_index - start_index):
                square = start_index + i
                if not empty_square(square):
                    return False

    # move is not horizontal or vertical
    else:   return False

    return True
        
# returns if a square is occupied or not
def empty_square(square):
    if square == 44: return False
    else: return True