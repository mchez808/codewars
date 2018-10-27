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

    # doctests
    >>> alpha_seq('A')
    'A'

    https://www.codewars.com/kata/alphabetical-sequence/train/python
    """
    list_str = []
    list_str.extend(string)
    list_str.sort()

    list_str = ["A"]
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in list_str:
        number_of_trailing_letters = ALPHABET.find(letter.upper())
        # str_same_letter example: "Eeeee"
        str_same_letter = letter.upper() + letter.lower()*number_of_trailing_letters
        list_str.append(str_same_letter)
    output_string = ",".join(list_str)
    return output_string


if __name__ == '__main__':
    print("*"*20)
    print("running doctest...")
    print("*"*20)
    import doctest
    doctest.testmod()

print("chicken!")
