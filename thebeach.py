# Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 7 (every 6 will be followed by at
# least one 7). Return 0 for no numbers.

def sum67(nums):
    sum = 0
    i = 0
    for i in xrange(len(nums)):
        if nums[i] == 6:
            # don't add anything to sum
            # do increment the iterator
            i += 1
            # check if the next number is seven
            # keep checking until the next number is 7
            while nums[i] != 7:
                i += 1
            # then break out of this loop
            i += 1
            break
        else:
            sum += nums[i]
    return sum
