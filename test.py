class TicTacToeBoard:
    def __init__(self):
        self.board = [['-', '-', '-'] for _ in range(3)]
        self.move = True
        self.end = False

    def new_game(self):
        self.board = [['-', '-', '-'] for _ in range(3)]
        self.move = True
        self.end = False

    def get_field(self):
        return self.board

    def check_field(self):
        for x in range(3):
            if (self.board[0][x] == self.board[1][x] == self.board[2][x] or
                    self.board[x][0] == self.board[x][1] == self.board[x][2]) and self.board[x][1] != '-':
                self.end = True
                return self.board[0][x]

        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or
                self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[1][1] != '-':
            self.end = True
            return self.board[1][1]

        check = all(map(lambda x: all(map(lambda y: True if y != '-' else False, x)), self.board))

        if not check:
            return None

        else:
            self.end = True
            return 'D'

    def make_move(self, row, col):
        if self.end is False:
            row -= 1
            col -= 1
            if self.board[row][col] == '-':
                self.board[row][col] = 'X' if self.move else '0'
                self.move = not self.move
                proverka = self.check_field()

                if proverka is None:
                    return 'Продолжаем играть'

                elif proverka == 'D':
                    self.end = True
                    return 'Ничья'

                else:
                    return f'Победил игрок {proverka}'
            else:
                return f'Клетка {row + 1}, {col + 1} уже занята'
        else:
            return 'Игра уже завершена'
