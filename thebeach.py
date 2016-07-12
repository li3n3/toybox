# Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 7 (every 6 will be followed by at
# least one 7). Return 0 for no numbers.

def sum67(nums):
    sum = 0
    i = 0
    while i < len(nums):
        if nums[i] != 6:
            sum += nums[i]
            i += 1
            print "I added the number then incremented i"
        else:
            # don't add anything to sum
            # do increment the iterator
            i += 1
            print "I incremented a thing because the number was 6"
            # check if the next number is seven
            # keep checking until the next number is 7
            while nums[i] != 7:
                i += 1
                print "it's still not 7; I incremented the counter"
            # then increment i to get past the 7, and break out of this loop
            i += 1
            print "I incremented the counter and now we'll break"
    return sum
