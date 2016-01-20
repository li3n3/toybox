"""
Given three ints, a b c, return True if one of b or c is "close" (differing from
a by at most 1), while the other is "far", differing from both other values by 2
or more. Note: abs(num) computes the absolute value of a number.
"""

def close_far(a, b, c):
    if abs(b - a) < 2:
        bclose = True
    else:
        bclose = False
    if abs(b - a) >= 2 and abs(b - c) >= 2:
        bfar = True
    else:
        bfar = False

    if abs(c - a) < 2:
        cclose = True
    else:
        cclose = False
    if abs(c - a) >= 2 and abs(c - b) >=2:
        cfar = True
    else:
        cfar = False

    if (bclose == True and cfar == True) or (bfar == True and cclose == True):
        return True
    else:
        return False
