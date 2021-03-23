import time

tic = time.perf_counter()

def find_longest_string(list_of_strings):
    longest_string = None
    longest_string_len = 0
    for s in list_of_strings:
        if len(s) > longest_string_len:
            longest_string_len = len(s)
            longest_string = s
    return longest_string

tic = time.perf_counter()
list_of_strings = ['abc', 'python', 'dima']
print(find_longest_string(list_of_strings))
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.8f} seconds")

list_of_string_lens = [len(s) for s in list_of_strings]
list_of_string_lens = zip(list_of_strings, list_of_string_lens)
print(tuple(list_of_string_lens))


# large_list_of_strings = list_of_strings*1000
# print(find_longest_string(list_of_strings))
# toc = time.perf_counter()
# print(f"Downloaded the tutorial in {toc - tic:0.8f} seconds")
#
# large_list_of_strings = list_of_strings*100000000
# print(find_longest_string(list_of_strings))
# toc = time.perf_counter()
# print(f"Downloaded the tutorial in {toc - tic:0.8f} seconds")


