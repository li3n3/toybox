def in1to10(n, outside_mode):
    if n in range(1, 11) and not outside_mode:
        return True
    elif (n <= 1 or n >= 10) and outside_mode:
        return True
    else:
        return False

print in1to10(-1, False)
