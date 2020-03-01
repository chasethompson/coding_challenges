"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

"""

def square_digits(num):
    num = str(num)
    return list(map(int, num))

assert square_digits(9119) == 811181

"""
https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

"""

"""
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

"""

def Xbonacci(signature,n):
    result = signature[:]

    for x in range(n-len(signature)):
        current_fib = 0
        start = len(result) - len(signature)
        for y in result[start:]:
            current_fib += y
        result.append(current_fib)

    return result[:n]

    """
    https://www.codewars.com/kata/556deca17c58da83c00002db
    
    """

