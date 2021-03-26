import copy
import time
from functools import reduce
mapper = len

tic = time.perf_counter()

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def reducer(p, c):
    print(p, c)
    if p[1] > c[1]:
        return p
    return c

def chunks_mapper(chunk):
    mapped_chunk = map(mapper, chunk)
    mapped_chunk = zip(chunk, mapped_chunk)
    return reduce(reducer, mapped_chunk)


list_of_strings = ['crocadile','abc', 'python', 'dima']*100
list_of_strings.append("xxxxxxxxxxxx")
data_chunks = chunks(list_of_strings, 30)

#step 1:
mapped = map(chunks_mapper, data_chunks)
#step 2:
reduced = reduce(reducer, mapped)

print("\n")
print(reduced)

toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.8f} seconds")


# #step 1 compute the len of all strings
# mapped = map(mapper, list_of_strings)
# # print("applied map: " + str(list(copy.deepcopy(mapped))))
# mapped = zip(list_of_strings, mapped)
# # print("zip: " + str(list(copy.deepcopy(mapped))))
# #step 2 select the max value
# reduced = reduce(reducer, mapped)
