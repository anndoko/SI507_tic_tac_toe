# set up the board
board_lst = list(range(0,9))
def draw_board():
    print("----------")
    print(board_lst[0], "|", board_lst[1], "|", board_lst[2])
    print("----------")
    print(board_lst[3], "|", board_lst[4], "|", board_lst[5])
    print("----------")
    print(board_lst[6], "|", board_lst[7], "|", board_lst[8])
    print("----------")

# check the board and see if that is a valid if_valid_move
def if_valid_move(p_input):
    if type(board_lst[p_input]) == int:
        return True
    else:
        print("That's not a valid move. Please pick a cell again.\n\n")

# win conditions
win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

p1_symbol = "O"
p2_symbol = "X"

for cell in board_lst:
    # p1 makes a move
    p1_input = int(input("Player 1, please make a move:"))
    while not if_valid_move(p1_input):
        p1_input = int(input("Player 1, please try again:"))
    board_lst[p1_input] = p1_symbol
    draw_board()

    # p2 makes a move
    p2_input = int(input("Player 2, please make a move:"))
    while not if_valid_move(p2_input):
        p2_input = int(input("Player 2, please try again:"))
    board_lst[p2_input] = p2_symbol
    draw_board()
