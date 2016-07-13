# Given an array length 1 or more of ints, return the difference between the
# largest and smallest values in the array. Note: the built-in min(v1, v2) and
# max(v1, v2) functions return the smaller or larger of two values.

minmaxdiff([4, 2, 1, 6, 7])
[7, 6, 8, 5]

def minmaxdiff(nums):
    # could define smallest/largest with temp values, but that seems sloppier
    if len(nums) <= 2:
        # latter part looks awkward! but it returns an answer if length is 1
        return abs(nums[0] - nums[-1])
    else:
        smallest = min(nums[0], nums[1])
        largest = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
            elif nums[i] > largest:
                largest = nums[i]
            # else, pass, but that's just noise
        return largest - smallest

