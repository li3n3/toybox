# Write a program that prints out the numbers 1 to 100 (inclusive). If the
# number is divisible by 3, print Crackle instead of the number. If it's
# divisible by 5, print Pop. If it's divisible by both 3 and 5, print
# CracklePop. You can use any language.

# it works!

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print 'CracklePop'
    elif num % 3 == 0:
        print 'Crackle'
    elif num % 5 == 0:
        print 'Pop'
    else:
        print num
