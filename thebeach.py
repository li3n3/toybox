# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that come
# immediately after a 13 also do not count.

def sum13(nums):
    # create a variable to sum all the non-13-tinged numbers
    safe_sum = 0
    # create an iterator that will let us easily skip a couple items in a row;
    # still just an iterator the length of the nums list, though
    # it = iter(xrange(len(nums)))
    # for i in it:
    #     if nums[i] == 13:
    #         i = next(it)
    #         print('okay i skipped something')
    #         # pass
    #     else:
    #         safe_sum += nums[i]
    #         print('okay i added a number')
    # return safe_sum

    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            safe_sum += nums[i]
            i += 1

    return safe_sum
