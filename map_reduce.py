import copy
from functools import reduce
mapper = len

def reducer(p, c):
    print(p, c)
    if p[1] > c[1]:
        return p
    return c

list_of_strings = ['crocadile','abc', 'python', 'dima']


#step 1 compute the len of all strings
mapped = map(mapper, list_of_strings)
print("applied map: " + str(list(copy.deepcopy(mapped))))
mapped = zip(list_of_strings, mapped)
print("zip: " + str(list(copy.deepcopy(mapped))))
#step 2 select the max value
reduced = reduce(reducer, mapped)
print(reduced)