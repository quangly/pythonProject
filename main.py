
def isPalindrome(str):

    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str) - i - 1]:
            return False

    return True



    # # run loop from 0 to len/2
    #
    # for i in range(0, int(len(str)/2)):
    #     if str[i] != str[len(str) -i - 1]:
    #         return False
    # return True

"""
An efficient solution would need only one traversal i.e. O(n) on the longer string s1. Here we will start traversing the
 string s1 and maintain a pointer for string s2 from 0th index. For each iteration we compare the current character in s1
  and check it with the pointer at s2. If they match we increment the pointer on s2 by 1. And for every mismatch we set
  the pointer back to 0. We also keep a check when the s2 pointer value is equal to the length of string s2, if true we
  break and return the value (pointer of string s1 – pointer of string s2)
"""


def isSubstring(s2, s1):
    i = 0
    x = 0
    lengthString = len(s2)

    for i in range(lengthString):

        # reached end of s1
        if (x == len(s1)):
            break

        # matched character, increase index of search string to find next match
        if (s2[i] == s1[x]):
            x += 1

        # if not matched, reset index of search string to 0 to reset search again for next character in long string
        else:
            x = 0

    # if the last character of search string is less than the length of string means it never reached or matched
    if x < len(s1):
        return -1
    # matched, find first index of long string once matched is found with last consecutive character
    else:
        return i - x


"""Time complexity: O(m * n) where m and n are lengths of s1 and s2 respectively.
A nested loop is used the outer loop runs from 0 to N-M and inner loop from 0 to M so the complexity is O(m*n).
"""
def isSubstringOld(s1, s2):
    lengthSub = len(s1)
    lengthString = len(s2)

    for i in range(lengthString - lengthSub +1):

        for j in range(lengthSub):
            if (s2[i + j] != s1[j]):
                break

        if (lengthSub == j + 1):
            return i

    return -1


if __name__ == "__main__":
    s1 = "for"
    s2 = "geeksforgeeks"

    res = isSubstring(s2, s1)
    if res == -1:
        print("Not present")
    else:
        print("Present at index " + str(res))

    res = isPalindrome("racecar")
    print("Palindrome: " + str(res))
