# This file contains clever and advanced solutions that are not my own work,
# but they are the work I strive to produce. 

# 7 kyu

def alpha_seq(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for s in ''.join(sorted((string.lower()))):
        output += s.upper()
        output += s * alpha.find(s)
        output += ','
    return output.strip(',')

######## THE CREATIVE SOLUTION FROM CODEWARS ########
# def alpha_seq(s):
#     return ",".join( (c * (ord(c)-96)).capitalize() for c in sorted(s.lower()) )
#####################################################


def binary_array_to_number(arr):
    sum = 0

    leading_decimal = len(arr)
    for exponent_subtrahend, binary_digit in enumerate(arr):
        sum += binary_digit * (2**(leading_decimal-exponent_subtrahend-1))
    return sum

######## THE CREATIVE SOLUTION FROM CODEWARS ########
    # return int("".join(map(str, arr)), 2)
######## THE CREATIVE SOLUTION FROM CODEWARS ########
    # return int(''.join(str(a) for a in arr), 2)
#####################################################


# 6 kyu

def reverse_alternate(s):
  words = s.split()
  words[1::2] = [word[::-1] for word in words[1::2]]
  return ' '.join(words)


"""Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.
    invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
    invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
    invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.

https://www.codewars.com/kata/invert-values/train/python
"""

def invert(inputlist):
    return [-n for n in inputlist]
