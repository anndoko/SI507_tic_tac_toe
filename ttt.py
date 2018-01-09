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

# win conditions
win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
