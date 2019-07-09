X = 'X'
O = 'O'
E = ' '
LINES = [
    # horizontal lines
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    
    # vertical lines
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    
    # diagonals
    [0, 4, 8],
    [2, 4, 6],
]

FIELDS = ['a3', 'b3', 'c3', 'a2', 'b2', 'c2', 'a1', 'b1', 'c1']


class TicTacToeGame:
    def __init__(self):
        self.board = [E] * 9
        self.to_move = X

    def get_winner(self):
        """Return X or O when somebody wins, 'draw' for a draw,
        None if still not finished
        """
        
        for i1, i2, i3 in LINES:
            if self.board[i1] == self.board[i2] == self.board[i3] != E:
                return self.board[i1]
        if E in self.board:
            return None
        else:
            return 'draw'
    
    def show_board(self):
        print('''
       -----------
    3 | {} | {} | {} |
       -----------
    2 | {} | {} | {} |
       -----------
    1 | {} | {} | {} |
       -----------
        A   B   C
    '''.format(*self.board))
    
    def make_move(self):
        board = self.board
        to_move = self.to_move
        self.show_board()
        while True:
            field = input(f'Where to put {to_move}? ').lower().strip()
            try:
                i = FIELDS.index(field)
            except ValueError:
                print('This is an invalid field name.')
                continue
            if board[i] != E:
                print('This field is alredy taken.')
                continue
            break
        board[i] = to_move


game = TicTacToeGame()
game2 = TicTacToeGame()
while game.get_winner() is None:
    game.make_move()
    game.to_move = (O if game.to_move == X else X)
    
winner = game.get_winner()
game.show_board()
if winner == 'draw':
    print('The game is a draw.')
else:
    print(f'{winner} wins the game.')

    