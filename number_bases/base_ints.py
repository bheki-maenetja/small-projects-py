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