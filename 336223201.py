import game_of_life_interface
import numpy as np
import matplotlib.pyplot as plt


class GameOfLife(game_of_life_interface.GameOfLife):
    def __init__(self, size_of_board, board_start_mode, rules, rle, pattern_position):
        self.size_of_board = size_of_board
        self.board_start_mode = board_start_mode
        self.rules = rules
        self.rle = rle
        self.pattern_position = pattern_position
        self.board = self.game_board()

    def __repr__(self):
        return str(self.board)

    def game_board(self):
        if self.rle == '':
            start_mode = {1: [0.5, 0.5], 2: [0.8, 0.2], 3: [0.2, 0.8], 4: []}
            if self.board_start_mode in [1, 2, 3, 4]:
                board = np.random.choice([1, 0], (self.size_of_board, self.size_of_board), True, start_mode[self.board_start_mode])
            else:
                board = np.random.choice([1, 0], (self.size_of_board, self.size_of_board), True, start_mode[1])
            return board

    def update(self):
        pass

    def return_board(self):
        pass

    def save_board_to_file(self, file_name):
        plt.imsave(file_name, self.board)  # needs check

    def display_board(self):  # needs check
        plt.imshow(self.board)
        plt.show()

    def transform_rle_to_matrix(self, rle):
        pass


if __name__ == '__main__':
    print('write your tests here')  # don't forget to indent your code here!
    G1 = GameOfLife(15, 5, 2, "", 3)
    print(G1.board)
