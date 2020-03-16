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

"""

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

"""
sp = ['-','_']
def to_camel_case(text):
    if len(text) == 0:
      return text
    text = text.replace("_","-")
    s = text.split("-")
    for i in range(len(s)):
      if i == 0:
        continue
      else:
        s[i] = s[i].capitalize()
    res = "".join(i for i in s)
    return res

"""

https://www.codewars.com/kata/517abf86da9663f1d2000003/solutions/python

"""


"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

"""

def anagrams(word, words):
    return [_ for _ in words if sorted(_) == sorted(word)]

"""
https://www.codewars.com/kata/523a86aa4230ebb5420001e1
"""

"""
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

"""

from collections import OrderedDict

def solution(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

"""
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/solutions/python
"""

"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:
"""

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "{} likes this".format(names[0])
    elif len(names) == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], len(names)-2)

"""
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python
"""