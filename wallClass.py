

class Wall():
    idx: int
    col_start: int
    col_end: int

    def __init__(self, idx, col_start, col_end):
        self.idx = idx
        self.col_start = col_start
        self.col_end = col_end

    def print_data(self):
        print(f'wall.idx={self.idx}, ' \
              f'wall.column_start={self.col_start}' \
              f'wall.column_end={self.col_end}')
