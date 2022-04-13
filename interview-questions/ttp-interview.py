def sum_of_digits(string_of_digits):
    """ This function should return the sum of digits in a string """
    return sum(int(char) for char in string_of_digits if char.isdigit())


def square_numbers(n):
    while n >= 0:
        yield n * n
        n -= 1

sq_gen = square_numbers(5)

for sq_num in square_numbers(10):
    print(sq_num)
    

def sum_of_digit_words(numerical_word):
    word_dict = {
        "one": 1,
        "two": 2,
        "three": 3
    }
    
    numerical_word = numerical_word.lower()
    sub_string = ""
    return_value = 0
    
    while numerical_word != "":
        sub_string += numerical_word[0]
        numerical_word = numerical_word[1:]
        if sub_string in word_dict:
            return_value += word_dict[sub_string]
            sub_string = ""
    
    return return_value
    

assert sum_of_digits("1") == 1
assert sum_of_digits("123") == 6
assert sum_of_digits("333") == 9


assert sum_of_digit_words("one") == 1 
assert sum_of_digit_words("twothree") == 5 