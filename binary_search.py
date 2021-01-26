# Python3 code to implement iterative Binary 
# Search. 

# It returns location of x in given array arr 
# if present, else returns -1
# Time complexity T(n) = T(n/2) + c

def binarySearch(arr, l, r, x):

    while l <= r:

        mid = l + (r - 1) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # if x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    # if we reach here, then element was not present
    return -1

#  Driver code
arr = [2,3,4,10,40]
x = 10

result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

