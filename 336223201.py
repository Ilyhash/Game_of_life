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
        self.board = self.build_board()

    def __repr__(self):
        return self.board.tolist()

    def build_board(self):
        if self.rle == '':
            start_mode = {1: [0.5, 0.5], 2: [0.2, 0.8], 3: [0.8, 0.2]}
            if self.board_start_mode in [2, 3]:
                self.board = np.random.choice([0, 255], (self.size_of_board, self.size_of_board), True, start_mode[self.board_start_mode])
            elif self.board_start_mode == 4:
                self.board = np.zeros([self.size_of_board, self.size_of_board])
                self.pattern_position = [10, 10]
                self.add_gosper_gg()
            else:
                self.board = np.random.choice([0, 255], (self.size_of_board, self.size_of_board), True, start_mode[1])
        else:
            self.board = np.zeros([self.size_of_board, self.size_of_board])
            self.board[self.pattern_position[0]:len(rle), self.pattern_position[1]:len(rle[0])] = self.transform_rle_to_matrix(self.rle)
        return self.board

    def add_gosper_gg(self):
        j = self.pattern_position[0]
        i = self.pattern_position[1]
        self.board[i+5:i+7, j+0:j+2] = 255
        self.board[i + 3, j+12:j+14] = 255
        self.board[i + 3:i + 6, j+20:j + 22] = 255
        self.board[i + 1:i + 3, j + 24] = 255
        self.board[i + 2, j + 22] = 255
        self.board[i + 6, j + 22] = 255
        self.board[i + 6:i + 8, j + 24] = 255
        self.board[i + 5:i + 8, j + 10] = 255
        self.board[i + 9, j+12:j + 14] = 255
        self.board[i + 4, j+11] = 255
        self.board[i + 8, j+11] = 255
        self.board[i + 6, j + 14] = 255
        self.board[i + 4, j + 15] = 255
        self.board[i + 8, j + 15] = 255
        self.board[i + 5:i + 8, j + 16] = 255
        self.board[i + 6, j + 17] = 255
        self.board[i + 3:i + 5, j + 34:j + 36] = 255

    def return_board(self):
        board = self.board.tolist()
        for x in board:
            for i in range(len(board[0])):
                x[i] = int(x[i])
        return board

    def update(self):
        rules = self.rules.split('/')
        born = [int(num) for num in rules[0] if num.isdigit()]
        survive = [int(num) for num in rules[1] if num.isdigit()]
        new_board = self.board.copy()
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
    g1 = GameOfLife(100, 4, 'b3/s23', "", (10, 10))
    g1.display_board()
    print(g1.return_board())
    for i in range(90):
        g1.update()
    g1.display_board()

