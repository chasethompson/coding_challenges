def square_digits(num):
    num = str(num)
    return list(map(int, num))

assert square_digits(9119) == 811181