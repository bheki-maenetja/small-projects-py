# Backtracking Solution for the 16 diagonals problem - still in development
import tkinter as tk

window = tk.Tk()
window.aspect(1,1,1,1)
window.minsize(300, 300)

class BaseInt():
    def __init__(self, base) -> None:
        assert 1 <= base <= 10
        self._base = base
    
    def convert_num(self, num, partition=0):
        remainders = []
        div_mod = divmod(num, self._base)
        remainders.append(str(div_mod[1]))

        while div_mod[0] != 0:
            div_mod = divmod(div_mod[0], self._base)
            remainders.insert(0, str(div_mod[1]))
        
        num_str = "".join(remainders)

        if len(num_str) % partition != 0:
            str_len = (len(num_str) + partition) - (len(num_str) % partition)
        else:
            str_len = len(num_str)
        
        num_str = num_str.zfill(str_len)
        num_str = " ".join(
            [num_str[i:i+partition] for i in range(0, str_len, partition)]
        )
        
        return num_str
    
    def counter(self, n, partition=0):
        for i in range(n):
            yield self.convert_num(i, partition)

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
    
    def get_str_grid(self):
        grid = [[str(i) for i in row] for row in self._grid]
        grid_string = ""
        for row in grid:
            grid_string += " ".join(row) + "\n"
        return grid_string.strip("\n")
    
    def generate_grid_perms(self):
        n = 3 ** (self._grid_size ** 2)
        base3_int = BaseInt(3)
        for i in base3_int.counter(n, 3):
            print(i)
    
    def __repr__(self) -> str:
        return self.get_str_grid()

if __name__ == "__main__":
    new_board = Board(3)
    new_board.generate_grid_perms()