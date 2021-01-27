# Python3 code to implement iterative Binary 
# Search. 

# It returns location of x in given array arr 
# if present, else returns -1
# Time complexity T(n) = T(n/2) = Log
#

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint_index = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint_index]

        if midpoint_value == item:
            return midpoint_index

        elif item < midpoint_value:
            end_index = midpoint_index - 1
        else:
            begin_index = midpoint_index + 1

    return None

sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
item_a = 12

print(binary_search(sequence_a, item_a))