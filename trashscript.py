def near_ten(num):
    if (num % 10) > 2 and (num % 10) < 8:
        print "num % 10 is {0}".format(num % 10)
        # meow
        return False
    else:
        return True

print near_ten(12)
