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
        self.board = self.return_board()

    def __repr__(self):
        return str(self.board)

    def return_board(self):
        if self.rle == '':
            start_mode = {1: [0.5, 0.5], 2: [0.2, 0.8], 3: [0.8, 0.2]}
            if self.board_start_mode in [2, 3]:
                board = np.random.choice([0, 255], (self.size_of_board, self.size_of_board), True, start_mode[self.board_start_mode])
            elif self.board_start_mode == 4:
                board = np.zeros([self.size_of_board, self.size_of_board])
                self.pattern_position = [10, 10]
                self.board.add_gosper_gg()
            else:
                board = np.random.choice([0, 255], (self.size_of_board, self.size_of_board), True, start_mode[1])
        return board

    def add_gosper_gg(self):
        gosper_glider_gun = self.transform_rle_to_matrix(rle='24bo11b$22bobo11b$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o14b$2o8bo3bob2o4bobo11b$10bo5bo7bo11b$11bo3bo20b$12b2o!')
        i = self.pattern_position[0]
        j = self.pattern_position[1]
        self.board[i:i+36, j:j+9] = gosper_glider_gun

    def update(self):
        rules = self.rules.split('/')
        born = [int(num) for num in rules[0] if num.isdigit()]
        survive = [int(num) for num in rules[1] if num.isdigit()]
        new_board = self.board
        for i in range(self.size_of_board):
            for j in range(self.size_of_board):
                neighbours = int((self.board[(i - 1) % self.size_of_board, (j - 1) % self.size_of_board] +
                    self.board[(i - 1) % self.size_of_board, j] + self.board[(i - 1) % self.size_of_board, (j + 1) % self.size_of_board] +
                    self.board[i, (j - 1) % self.size_of_board] + self.board[i, (j + 1) % self.size_of_board] +
                    self.board[(i + 1) % self.size_of_board, (j - 1) % self.size_of_board] + self.board[(i + 1) % self.size_of_board, j] +
                    self.board[(i + 1) % self.size_of_board, (j + 1) % self.size_of_board]) / 255)
                if (self.board[i, j] == 0 and neighbours in born) or (self.board[i, j] == 255 and neighbours in survive):
                    new_board[i, j] = 255
                else:
                    new_board[i, j] = 0
        self.board = new_board

    def save_board_to_file(self, file_name):
        plt.imsave(file_name, self.board)  # needs check

    def display_board(self):
        plt.imshow(self.board)
        plt.show()

    def transform_rle_to_matrix(self, rle):
        pass


if __name__ == '__main__':
    print('write your tests here')  # don't forget to indent your code here!
    g1 = GameOfLife(100, 3, 'b3/s23', "", 3)
    for i in range(10):
        g1.display_board()
        g1.update()


