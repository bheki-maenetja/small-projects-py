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

# from random import randint
# my_list = [i for i in range(1, 102)]
# list_subsets = (my_list[i:i+7] for i in range(0, len(my_list), 7))
# for i, subset in enumerate(list_subsets):
#     print(i, subset)