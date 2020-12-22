def check_even(num):
    if num == 0:
        return False
    elif num % 2 == 0:
        return True
    else:
        return False

assert check_even(8) == True
assert check_even(0) == False
assert check_even(55) == False
