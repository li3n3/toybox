"""
Return the number of times that the string "hi" appears anywhere in the given
string.
"""

def count_hi(str):
    count = 0
    for index in range(0, len(str) - 1):
        if str[index] + str[index + 1] == 'hi':
            count += 1

    return count
