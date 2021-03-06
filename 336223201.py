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
                self.rle = "24bo11b$22bobo11b$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o14b$2o8bo3bob2o4bobo11b$10bo5bo7bo11b$11bo3bo20b$12b2o!"
                self.build_board()
            else:
                self.board = np.random.choice([0, 255], (self.size_of_board, self.size_of_board), True, start_mode[1])
        else:
            self.board = np.zeros([self.size_of_board, self.size_of_board])
            shape = self.transform_rle_to_matrix()
            self.board[self.pattern_position[0]: self.pattern_position[0] + len(shape),
            self.pattern_position[1]: self.pattern_position[1] + len(shape[0])] = np.array(shape)
        return self.board

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

    def transform_rle_to_matrix(self):
        rle = self.rle.split('$')
        rle[-1] = rle[-1][:-1]
        matrix = []
        values = {'b': [0], 'o': [255]}
        for row in rle:
            vector = []
            index = 0
            letters = []
            for i in range(len(row)):
                if row[i].isalpha():
                    letters.append(i)
            for letter in letters:
                if letter - index >= 1:
                    to_add = int(row[index: letter]) * values[row[letter]]
                    vector.extend(to_add)
                    index = letter + 1
                else:
                    vector.extend(values[row[letter]])
                    index = letter + 1
            matrix.append(vector)
            if index < len(row):
                matrix.extend([[0] * len(vector)] * (int(row[index: len(row)]) - 1))
        diff = len(matrix[0]) - len(matrix[-1])
        if diff > 0:
            matrix[-1].extend([0] * diff)
        return matrix


if __name__ == '__main__':
    print('write your tests here')  # don't forget to indent your code here!
    g1 = GameOfLife(100, 4, 'b3/s23', "7bo6b$6bobo5b$7bo6b2$5b5o4b$4bo5bob2o$3bob2o3bob2o$3bobo2bobo3b$2obo3b2obo3b$2obo5bo4b$4b5o5b2$6bo7b$5bobo6b$6bo!", (10, 10))
    g1.display_board()
    print(g1.return_board())
    for i in range(90):
        g1.update()
    g1.display_board()
