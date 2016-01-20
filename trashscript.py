""" Return the number of times that the string "code" appears anywhere in the
given string, except we'll accept any letter for the 'd', so "cope" and "cooe"
count.
"""

def count_code(str):
    codecount = 0
    for num in range(0, len(str) - 3):
        print "okay this time num is {}".format(num)
        # look for a c at that index
        if str[num] == 'c':
        # if you find it, look for an o
            if str[num + 1] == 'o':
        # the next letter is fine, no matter what
        # so conveniently we don't have to do anything
        # look for an e
                if str[num + 3] == 'e':
        # if you got this far, increment counter by 1
                    codecount += 1
        # and repeat!

        # return codecount
    return codecount
