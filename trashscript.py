"""
Return True if the string "cat" and "dog" appear the same number of times in the
given string.
"""

def cat_dog(str):
    catcount = 0
    dogcount = 0
    # iterate through each character
    for index in range(0, len(str) - 2):
        # if the char, plus the two after, == cat
        if str[index:index+3] == 'cat':
            # catcount goes up one
            catcount += 1
        # elif the char, plus the two after, == dog
        elif str[index:index+3] == 'dog':
            # dogcount goes up one
            dogcount += 1

    # return the truth of whether catcount == dogcount
    return catcount == dogcount
