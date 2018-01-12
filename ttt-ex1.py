# function: print current board
# params: the draw_board function does not take any input as its parameter
# return: the draw_board function does not return anything; it prints the current board for the players
def draw_board():
    print("CURRENT BOARD:")
    print("----------")
    print(board_lst[0], "|", board_lst[1], "|", board_lst[2])
    print("----------")
    print(board_lst[3], "|", board_lst[4], "|", board_lst[5])
    print("----------")
    print(board_lst[6], "|", board_lst[7], "|", board_lst[8])
    print("----------")

# function: prompt the player for input
# params: the player_move function does not take any input as its parameter
# return: the player_move function returns an integer
def player_move():
    while True:
        try:
            player_input = int(input("Please make a move:"))
            return player_input
            break
        except ValueError:
            print("Please enter the cell number.")

# function: check the board and see if that is a valid if_valid_move
# params: the if_valid_move function takes an integer as its parameter
# return: the if_valid_move function returns True if the move is valid
def if_valid_move(p_input):
    if type(board_lst[p_input]) == int:
        return True
    else:
        print("That's not a valid move. Please pick a cell again:\n")

# function: check if the player wins the game
# params: the if_win function does not take any input as its parameter
# return: the if_win function returns True if any of the win combination is found
def if_win():
    # win combinations
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    # iterate through the list of win combinations
    for cell_1, cell_2, cell_3 in win_combinations:
        if board_lst[cell_1] == board_lst[cell_2] and board_lst[cell_2] == board_lst[cell_3]:
            print("Congradulations. You win!")
            return True

# function: check if it is a tie
# params: the if_draw function does not take any input as its parameter
# return: the if_draw returns False if it finds an available cell; otherwise, it returns True
def if_draw():
    for cell in board_lst:
        if type(cell) == int:
            return False
    print("It is a tie.")
    return True


# ---------------------------------------
# create a list from 0 to 8 for the board
board_lst = list(range(0,9))

# players' symbols
p1_symbol = "O"
p2_symbol = "X"

for cell in board_lst:
    # p1 makes a move
    p1_input = player_move()
    while not if_valid_move(p1_input):
        p1_input = player_move()
    board_lst[p1_input] = p1_symbol
    draw_board()
    # after p1 made the move, check if p1 wins the game
    # if the returned value is True, break the loop
    if if_win() or if_draw():
        break
    # p2 makes a move
    p2_input = player_move()
    while not if_valid_move(p2_input):
        p2_input = player_move()
    board_lst[p2_input] = p2_symbol
    draw_board()
    # after p2 made the move, check if p2 wins the game
    # if the returned value is True, break the loop
    if if_win() or if_draw():
        break
