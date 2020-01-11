from src.board import Board
from src.player import Player

class TicTacToe():

    def __init__(self):
        self.board = Board()
        self.player1 = Player("X", input("Player 1, enter your name: "))
        self.player2 = Player("O", input("Player 2, enter your name: "))
        self.currentPlayer = self.player1
        

    def game_start(self):
        while True:
            self.board.print_board()
            position = int(input(f'{self.currentPlayer.name} Please enter a number 1..9: '))
            err_msg = self.board.valid_position(position)
            while err_msg:
                print(err_msg)
                position = int(input(f'{self.currentPlayer.name} Please enter a number 1..9: '))
                err_msg = self.board.valid_position(position)
            self.board.add_piece(self.currentPlayer.piece, position)
            if (self.board.winning_state()):
                self.board.print_board()
                print(f'Congratulation {self.currentPlayer.name}!! You have won the game')
                break
            if self.board.full_board():
                self.board.print_board()
                print("The game is a tie!")
                break
            if self.currentPlayer is self.player1:
                self.currentPlayer = self.player2
            else:
                self.currentPlayer = self.player1
