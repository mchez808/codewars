# 7 kyu

def alpha_seq(string):
    """In this kata you will be given a random string of letters and tasked with
    returning them as a string of comma-separated sequences sorted alphabetcally,
    with each sequence starting with an uppercase character followed by n-1
    lowercase characters, where n is the letter's alphabet position 1-26.

    Example
    alpha_seq("ZpglnRqenU") -> "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Zzzzzzzzzzzzzzzzzzzzzzzzzz"

    Technical Details:
    - The string will include only letters.
    - The first letter of each sequence is uppercase followed by n-1 lowercase.
    - Each sequence is seperated with a comma.
    - Return value needs to be a string.

    https://www.codewars.com/kata/alphabetical-sequence/train/python
    """
    list_out, list_str = [], []
    list_str.extend(string.upper())
    list_str.sort()

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in list_str:
        number_of_trailing_letters = ALPHABET.find(letter)
        # str_same_letter example: "Eeeee"
        str_same_letter = letter.upper() + letter.lower()*number_of_trailing_letters
        list_out.append(str_same_letter)
    output_string = ",".join(list_out)
    return output_string


def binary_array_to_number(arr):
    """
    Given an array of one's and zero's convert the equivalent binary value to an integer.

    Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

    Examples:
        Testing: [0, 1, 0, 1] ==> 5
        Testing: [1, 0, 0, 1] ==> 9
        Testing: [1, 0, 0, 1, 0] ==> 34
        Testing: [1, 0, 0, 0, 0, 0, 0, 0] ==>

    However, the arrays can have varying lengths, not just limited to 4.

    https://www.codewars.com/kata/ones-and-zeros/train/python
    """
    sum = 0

    leading_decimal = len(arr)
    for exponent_subtrahend, binary_digit in enumerate(arr):
        sum += binary_digit * (2**(leading_decimal-exponent_subtrahend-1))
    return sum
