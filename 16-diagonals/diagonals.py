# Backtracking Solution for the 16 diagonals problem - still in development
import tkinter as tk

window = tk.Tk()
window.aspect(1,1,1,1)
window.minsize(300, 300)

class BaseInt():
    """
    Class for representing integers in a given base
    """
    def __init__(self, base) -> None:
        assert 1 <= base <= 10
        self._base = base
    
    def convert_num(self, num, partition=0, min_str_len=None):
        """
        PARAMETERS
            * num -> positive base 10 integer to be converted to the given base
            * partition -> the size of each partition in the return string
            * min_str_len -> the minimum length of the return string
        RETURN VALUES
            * num_str -> a bit string that represents num in the given base
        WHAT DOES THIS FUNCTION DO?
            * Converts a positive base 10 integer to the same number but in a 
              different base
        """
        remainders = []
        div_mod = divmod(num, self._base)
        remainders.append(str(div_mod[1]))

        while div_mod[0] != 0:
            div_mod = divmod(div_mod[0], self._base)
            remainders.insert(0, str(div_mod[1]))
        
        num_str = "".join(remainders)

        if min_str_len:
            str_len = min_str_len
        elif len(num_str) % partition != 0:
            str_len = (len(num_str) + partition) - (len(num_str) % partition)
        else:
            str_len = len(num_str)
        
        num_str = num_str.zfill(str_len)
        num_str = " ".join(
            [num_str[i:i+partition] for i in range(0, str_len, partition)]
        )
        
        return num_str
    
    def counter(self, n, partition=0, min_str_len=None):
        for i in range(n):
            yield self.convert_num(i, partition, min_str_len)

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
        n = 3 ** (self._grid_size ** 2)
        base_int = BaseInt(self._grid_size)
        for num_str in base_int.counter(n, self._grid_size, self._grid_size ** 2):
            print("New Grid >>>>>")
            print(self.grid_to_str(self.str_to_grid(num_str)))
    
    def __repr__(self) -> str:
        return self.grid_to_str(self._grid)

if __name__ == "__main__":
    new_board = Board(3)
    new_board.generate_grid_perms()