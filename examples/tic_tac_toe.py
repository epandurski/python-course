PLAYER_X = 'X'
PLAYER_O = 'O'
NO_PLAYER = ' '
LINES = [
    # horizontals
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],

    # verticals
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],

    # diagonals
    [0, 4, 8],
    [2, 4, 6],
]
FIELD_NAMES = ['A3', 'B3', 'C3', 'A2', 'B2', 'C2', 'A1', 'B1', 'C1']


def get_winner(board):
    """Return the winner, or `None` if the game is not finished yet."""

    for indexes in LINES:
        field1, field2, field3 = [board[i] for i in indexes]
        if field1 == field2 == field3 != NO_PLAYER:
            return field1  # We have a winner.
    if NO_PLAYER not in board:
        return NO_PLAYER  # The game is draw.


def make_move(player, board):
    """Ask `player` to play a move on the `board`."""

    while True:
        field_name = input('On which field to put {}? '.format(player))
        try:
            index = FIELD_NAMES.index(field_name.upper())
            if board[index] == NO_PLAYER:
                board[index] = player
                break
        except ValueError:
            pass
        print('Invalid field.')


def get_next_player(player):
    if player == PLAYER_X:
        return PLAYER_O
    return PLAYER_X


def show_board(board):
    print("""
       -----------
    3 | {} | {} | {} |
       -----------
    2 | {} | {} | {} |
       -----------
    1 | {} | {} | {} |
       -----------
        A   B   C
    """.format(*board))


# Play the game.
board = 9 * [NO_PLAYER]
to_move = PLAYER_X
winner = None
while winner is None:
    show_board(board)
    make_move(to_move, board)
    winner = get_winner(board)
    to_move = get_next_player(to_move)

# Show the winner.
show_board(board)
if winner == NO_PLAYER:
    print('The game is draw!')
else:
    print('"{}" wins the game!'.format(winner))
