# 7 kyu

def reverse_alternate(string):
    """
    Reverse every other word in the string

    Reverse every other word in a given string, then return the string.
    Throw away any leading or trailing whitespace, while ensuring there is
    exactly one space between each word. Punctuation marks should be treated
    as if they are apart of the word in this kata.

    https://www.codewars.com/kata/reverse-every-other-word-in-the-string/train/python
    """
    list_str = string.split()
    list_output = []

    for i in range(0, len(list_str)):
        if i % 2 == 0:
            this_str = list_str[i]
        else:
            this_str = list_str[i][::-1]
        list_output.append(this_str)
    output_string = " ".join(list_output)
    return output_string


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
