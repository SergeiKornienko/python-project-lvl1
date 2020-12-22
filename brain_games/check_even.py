def check_even(num):
    if num == 0:
        return 'no'
    elif num % 2 == 0:
        return 'yes'
    else:
        return 'no'


assert check_even(8) == 'yes'
assert check_even(0) == 'no'
assert check_even(55) == 'no'
