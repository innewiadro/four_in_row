import sys
EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

BOARD_WIDTH = 7
BOARD_HEIGHT = 6

COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")

BOARD_TEMPLATE = """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|"""


def get_new_board():
    pass


def display_board():
    pass


def get_player_move():
    pass


def is_winner():
    pass


def is_full():
    pass


def main():
    print("TODO")
    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:
        display_board(game_board)
        player_move = get_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        if is_winner(player_turn, game_board):
            display_board(game_board)
            print("Player {} win".format(player_turn))
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)
            print("Draw")
            sys.exit()

        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X



if __name__ == "__main__":
    main()