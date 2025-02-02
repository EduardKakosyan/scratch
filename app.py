import numpy as np


class GridWorldPolicy:
    pass


class Grid:
    def __init__(self, row_size=2, col_size=2, matrix=None) -> None:
        if matrix is not None:
            self.matrix = np.array(matrix)
            self.row_size, self.col_size = self.matrix.shape
        else:
            self.row_size = row_size
            self.col_size = col_size
            self.matrix = np.zeros((row_size, col_size))

    def set_start_position(self, row: int, col: int) -> None:
        if row >= self.row_size or col >= self.col_size:
            print("Can't set start position, it is out of range")
            return

        self.matrix[row][col] = 69

    def print_grid(self) -> None:
        print("-" * (self.col_size * 8))

        for i in range(self.row_size):
            row_str = (
                "| "
                + " | ".join(f"{self.matrix[i][j]:^5}" for j in range(self.col_size))
                + " |"
            )
            print(row_str)
            print("-" * (self.col_size * 8))


if __name__ == "__main__":
    preset_values = [[1, 2], [3, 4]]
    test_grid = Grid(matrix=preset_values)

    test_grid.print_grid()
