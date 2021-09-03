# Backtracking Solution for the 16 diagonals problem - still in development
import tkinter as tk

window = tk.Tk()
window.aspect(1,1,1,1)
window.minsize(300, 300)

class Board():
    def __init__(self, grid_size=5, num_diagonals=16) -> None:
        self._window = tk.Tk()
        self._window.aspect(1,1,1,1)
        self._window.minsize(300, 300)
        self._grid_size = grid_size
        self._num_diagonals = num_diagonals
        self._grid = [[0 for i in range(grid_size)] for i in range(grid_size)]
    
    def get_grid(self):
        return self._grid
    
    def grid_to_str(self, grid):
        """
        PARAMETERS
            * grid -> a 2D array representing a grid
        RETURN VALUES
            * a string representing the values of the grid
        """
        grid_string = ""
        for row in grid:
            grid_string += " ".join([str(i) for i in row]) + "\n"
        return grid_string.strip("\n")
    
    def str_to_grid(self, bit_string):
        """
        PARAMETERS
            * bit_string -> string representing a number in a given base
        RETURN VALUES
            * an 2D array of integers representing bit_string
        WHAT DOES THIS FUNCTION DO?
            * generates one permutation of a grid based on a given bit string
        """
        return [
            [int(i) for i in num_string] for num_string in bit_string.split(" ")
        ]
    
    def generate_grid_perms(self):
        """
        PARAMETERS
            * None
        RETURN VALUES
            * None
        WHAT DOES THIS FUNCTION DO?
            * generates all possible configurations of a grid
        """
        n = 3 ** (self._grid_size ** 2)
        base_int = BaseInt(3)
        for num_str in base_int.counter(n, self._grid_size, self._grid_size ** 2):
            yield self.str_to_grid(num_str)
    
    def row_valid(self, row):
        if len(row) == 1:
            return True
        
        return not any(
            (i + j) == 0 for i, j in zip(row[:-1], row[1:]) if i != 0 and j != 0
        )
    
    def grid_valid(self, grid):
        if len(grid) == 1:
            return self.row_valid(grid[0])
        
        if not all(self.row_valid(row) for row in grid):
            return False
        
        for row1, row2 in zip(grid[:-1], grid[1:]):
            touching_diagonals = any(
                abs(i + j) == 2 for i, j in zip(row1[1:], row2[:-1]) if i != 0 and j != 0
            ) or any(
                (i + j) == 2 for i, j in zip(row1[:-1], row2[1:]) if i != 0 and j != 0
            )

            if touching_diagonals:
                return False
        
        return True

    def place_diagonals(self, perm):
        if len(perm) == self._grid_size and all(len(row) == 5 for row in perm):
            print(self.grid_to_str(self._grid))
            return
        
        for i in range(self._grid_size):
            new_row = []
            for i in range(-1, 2):
                new_row.append(i)
                print(new_row)
                if not self.row_valid(new_row):
                    new_row.pop()
            perm.append(new_row)
            if not self.grid_valid(perm):
                perm.pop()
        
        print(perm)
        # print(self.grid_to_str(perm))

    def __repr__(self) -> str:
        return self.grid_to_str(self._grid)

if __name__ == "__main__":
    new_board = Board(3)
    new_board.place_diagonals([])