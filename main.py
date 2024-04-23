class Sudoku:
    def __init__(self, in_board=None):
        self.board = [[None for _ in range(9)] for _ in range(9)]
        if in_board is not None:
            self.from_string(in_board)

    def from_string(self, in_str):
        for i, row in enumerate(in_str.split()):
            for j, cell in enumerate(row):
                if cell in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                    self.board[i][j] = int(cell)

    def __str__(self):
        out = ""
        for i in range(9):
            for j in range(9):
                if type(self.board[i][j]) is int:
                    out += str(self.board[i][j])
                elif len(self.poss(i, j)) == 2:
                    out += 'o'
                else:
                    out += '.'
            out += '\n'

        return out

    def poss(self, i, j):
        return {}


test_board_easy = '72.5....3\n.....61..\n9.63.4...\n874.53.69\n6.5.28731\n....974..\n..27.....\n46....51.\n.....5.26'


def main():
    test = Sudoku(in_board=test_board_easy)
    print(test)


if __name__ == '__main__':
    main()

