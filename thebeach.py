# Given an array of ints, return True if the array contains a 2 next to a 2
# somewhere.

def has22(nums):
    for i in range (1, len(nums)):
        if nums[i-1] == 2 and nums[i] == 2:
            return True
    # this will only happen if the if statement above is never True
    return False
