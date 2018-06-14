import sys
import pygame


class TicTacToeGame:
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

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tic tac toe')
        self.screen = pygame.display.set_mode([800, 600])
        self.width, self.height = self.screen.get_size()
        self.line_thickness = min(self.width, self.height) // 80
        self.clock = pygame.time.Clock()
        self.restart_game()

    def restart_game(self):
        self.board = 9 * [self.NO_PLAYER]
        self.to_move = self.PLAYER_X
        self.winner = None
        pygame.mouse.set_visible(False)

    def try_to_make_move(self, field_index):
        if self.board[field_index] == self.NO_PLAYER:
            self.board[field_index] = self.to_move
            self.winner = self.get_winner()
            self.to_move = self.get_next_player()

    def get_winner(self):
        """Return the winner, or `None` if the game is not finished yet."""

        for indexes in self.LINES:
            field1, field2, field3 = [self.board[i] for i in indexes]
            if field1 == field2 == field3 != self.NO_PLAYER:
                return field1  # We have a winner.
        if self.NO_PLAYER not in self.board:
            return self.NO_PLAYER  # The game is draw.

    def get_next_player(self):
        if self.to_move == self.PLAYER_X:
            return self.PLAYER_O
        return self.PLAYER_X

    def draw_field(self, field, x, y, color=(0, 0, 0)):
        assert field in [self.PLAYER_X, self.PLAYER_O, self.NO_PLAYER]
        radius = 10 * self.line_thickness
        if field == self.PLAYER_O:
            pygame.draw.circle(self.screen, color, (x, y), radius, self.line_thickness)
        elif field == self.PLAYER_X:
            top_left = x - radius, y - radius
            bottom_right = x + radius, y + radius
            top_right = x - radius, y + radius
            bottom_left = x + radius, y - radius
            pygame.draw.line(self.screen, color, top_left, bottom_right, self.line_thickness)
            pygame.draw.line(self.screen, color, top_right, bottom_left, self.line_thickness)

    def draw_empty_board(self):
        self.screen.fill((255, 255, 255))
        dx = self.width // 3
        dy = self.height // 3
        lines = [
            ((1 * dx, 0), (1 * dx, self.height)),
            ((2 * dx, 0), (2 * dx, self.height)),
            ((0, 1 * dy), (self.width, 1 * dy)),
            ((0, 2 * dy), (self.width, 2 * dy)),
        ]
        for line in lines:
            pygame.draw.line(self.screen, (0, 0, 0), *line, self.line_thickness)

    def draw_winner(self):
        assert game.winner
        if game.winner == self.NO_PLAYER:
            message = 'The game is draw!'
        else:
            message = '"{}" wins the game!'.format(game.winner)
        font = pygame.font.Font(None, self.width // 10)
        text = font.render(message, 1, (255, 128, 0))
        text_position = text.get_rect()
        text_position.centerx = self.width // 2
        text_position.centery = self.height // 2
        self.screen.blit(text, text_position)

    def draw_board(self):
        self.draw_empty_board()

        # Draw the played "X"s an "O"s.
        dx = self.width // 3
        dy = self.height // 3
        for index, field in enumerate(self.board):
            i, j = divmod(index, 3)
            center_x = dx * j + dx // 2
            center_y = dy * i + dy // 2
            self.draw_field(field, center_x, center_y)

        if game.winner:
            self.draw_winner()
            pygame.mouse.set_visible(True)
        elif pygame.mouse.get_focused():
            # Draw the symbol of the player to move.
            self.draw_field(self.to_move, *pygame.mouse.get_pos(), color=(255, 128, 0))

    def wait_for_events(self):
        pygame.display.update()
        self.clock.tick(20)

    def process_mouse_click(self, x, y):
        if self.winner:
            self.restart_game()
        else:
            dx = self.width // 3
            dy = self.height // 3
            field_index = x // dx + 3 * (y // dy)
            self.try_to_make_move(field_index)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.process_mouse_click(*event.pos)


game = TicTacToeGame()
while True:
    game.draw_board()
    game.wait_for_events()
    game.process_events()
