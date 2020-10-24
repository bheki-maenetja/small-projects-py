def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    return "".join(i for i in s if i.lower() not in 'aeiou')

# print(print_without_vowels("This is great!"))
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    if set(L1) != set(L2) or len(L1) != len(L2):
        return False
    elif L1 == [] and L2 == []:
        return (None, None, None)
    else:
        l1_set = { (y, L1.count(y)) for y in L1 }
        l2_set = { (y, L2.count(y)) for y in L2 }
        if l1_set != l2_set:
            return False
        else:
            common_element = max(l1_set, key=lambda x: x[1])
            return (common_element[0], common_element[1], type(common_element[0]))

# l1 = [1, 'b', 1, 'c', 'c', 1]
# l2 = ['c', 1, 'b', 1, 1, 'c']
# print(is_list_permutation(l1, l2))
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

def f(a, b):
    return a + b

def g(a, b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    diff_keys = d1_keys.symmetric_difference(d2_keys)
    return (
        { key: f(d1[key], d2[key]) for key in intersect_keys },
        { key: (d1[key] if d1.get(key) != None else d2[key]) for key in diff_keys },
    )

print(dict_interdiff(d1, d2))
