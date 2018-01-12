# function: print current board
# params: the draw_board function takes a list as its parameter
# return: the draw_board function does not return anything; it prints the current board for the players
def draw_board(board_lst):
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

# function: if the move is valid, mark the cell with that player's symbol
# params: the mark_cell function takes p_number (int) and p_move (int) as its params
# returns: the mark_call function does not return anything
def mark_cell(p_number, p_move):
    if p_number == 1:
        board_lst[p_move] = "O"
    if p_number == 2:
        board_lst[p_move] = "X"

# function: check if the player wins the game
# params: the if_win function takes a list as its parameter
# return: the if_win function returns True if any of the win combination is found
def if_win(board_lst):
    # win combinations
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    # iterate through the list of win combinations
    for cell_1, cell_2, cell_3 in win_combinations:
        if board_lst[cell_1] == board_lst[cell_2] and board_lst[cell_2] == board_lst[cell_3]:
            print("Congradulations. You win!")
            return True

# function: check if it is a tie
# params: the if_draw function takes a list as its parameter
# return: the if_draw returns False if it finds an available cell; otherwise, it returns True
def if_draw(board_lst):
    for cell in board_lst:
        if type(cell) == int:
            return False
    print("It is a tie.")
    return True

# ---------- GAME SET-UP ----------
board_lst = list(range(0,9)) # create a list from 0 to 8 for the board
turn = 0 # turn
p_number = 0 # player's number

# ---------- GAME ----------
while turn < 9:
    # tell which player's playing
    if turn % 2 == 0:
        p_number = 1
    else:
        p_number = 2

    # prompt the player for input
    print("Player {}, it's your turn.".format(p_number))
    draw_board(board_lst) # print the board
    p_move = player_move()
    while not if_valid_move(p_move): # validate the move
        p_move = player_move()
    mark_cell(p_number, p_move) # mark the cell if the move is valid
    draw_board(board_lst)
    print("\n")
    if if_win(board_lst) or if_draw(board_lst): # check win/tie
        break # if yes, end the game

    turn += 1
