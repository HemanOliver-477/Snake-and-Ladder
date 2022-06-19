# SNAKE AND LADDER GAME
import pygame
import random

screen = pygame.display.set_mode((1024, 1024))
board_img = pygame.image.load('board_img.webp')

# RGB COLOR CODES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (169, 169, 169)
LIGHT_GREEN = (144, 238, 144)
LIGHT_BLUE = (173, 216, 230)

COLORS = [RED, BLACK, WHITE, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, LIGHT_GRAY, DARK_GRAY, LIGHT_GREEN, LIGHT_BLUE]

class Player:
    def __init__(self, pos_board) -> None:
        self.name = input("Enter your name: ")
        self.pos = pos_board
        self.row = 0
        self.col = 0
        self.num_to_row_col()
        self.x = self.col * 100 - 100
        self.y = 1000 - ((self.row - 1) * 100)
        self.color = COLORS.pop(random.randint(0, len(COLORS) - 1))

    def dice_roll(self) -> None:
        return random.randint(1, 6)

    def draw(self):
        # Draw player circle
        self.x = self.col * 100 - 100
        self.y = 1000 - ((self.row - 1) * 100)
        pygame.draw.circle(screen, self.color, (self.x + 50, self.y - 40), 30)

    def num_to_row_col(self):
        if (self.pos % 10 == 0):
            self.row = self.pos // 10
        else:
            self.row = (self.pos // 10) + 1
        if (self.row % 2 == 1):
            if (self.pos % 10 == 0):
                self.col = 10
            else:
                self.col = self.pos % 10
        else:
            if self.pos % 10 == 0:
                self.col = 1
            else:
                self.col = 11 - (self.pos % 10)
    
    def __str__(self) -> str:
        return "I'm there!"

class Game():
    def __init__(self) -> None:
        self.players = []
        self.gameOver = False
        self.snake_pos = {17: 7, 54: 34, 62: 19, 64: 60, 87: 36, 93: 73, 95: 75, 98: 79}
        self.ladder_pos = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72: 91, 80: 99}
        self.add_players()
        self.no_of_turns = len(self.players)

    def add_players(self):
        no_of_players = int(input("Enter number of players: "))
        for no in range(no_of_players):
            player = Player(0)
            print(player.row, player.col)
            self.players.append(player)

    def checkWin(self):
        for player in self.players:
            if player.row == 10 and player.col == 1:
                print("{} Wins".format(player.name))
                
    def isComplete(self):
        i = 0
        for player in self.players:
            if player.row == 10 and player.col == 1:
                i += 1
        if i == len(self.players):
            return True

    def draw_player(self):
        if len(self.players) > 0:
            for player in self.players:
                player.draw()

    def roll_dice(self, player_turn):
        player = self.players[player_turn]
        dice_value = player.dice_roll()
        if (player.pos + dice_value) <= 100:
            player.pos += dice_value
        if player.pos in self.snake_pos:
            player.pos = self.snake_pos[player.pos]
        elif player.pos in self.ladder_pos:
            player.pos = self.ladder_pos[player.pos]
        player.num_to_row_col()
        print(dice_value)
        print(player.pos)
        print(player.row, player.col)

    def change_turn(self, player_turn):
        player_turn += 1
        if player_turn == len(self.players):
            player_turn = 0
        return player_turn

run = True
turn = 0
game = Game()

# Game Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            game.roll_dice(turn)
            turn = game.change_turn(turn)
        elif (game.gameOver):
            pass

    screen.blit(board_img, (0, 0))
    game.draw_player()
    game.checkWin()
    pygame.display.update()
