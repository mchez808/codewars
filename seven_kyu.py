# 7 kyu

def alpha_seq(string):
    """In this kata you will be given a random string of letters and tasked with
    returning them as a string of comma-separated sequences sorted alphabetcally,
    with each sequence starting with an uppercase character followed by n-1
    lowercase characters, where n is the letter's alphabet position 1-26.

    Example
    alpha_seq("ZpglnRqenU") -> "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Zzzzzzzzzzzzzzzzzzzzzzzzzz"

    ___ alpha_seq('ZpglnRqenU')
    'Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Zzzzzzzzzzzzzzzzzzzzzzzzzz'

    Technical Details:
    - The string will include only letters.
    - The first letter of each sequence is uppercase followed by n-1 lowercase.
    - Each sequence is seperated with a comma.
    - Return value needs to be a string.

    # doctests
    >>> alpha_seq('A')
    'A'

    >>> alpha_seq('a')
    'A'

    >>> alpha_seq('B')
    'Bb'

    >>> alpha_seq('bb')
    'Bb,Bb'

    >>> alpha_seq('Cbc')
    'Ccc,Bb,Ccc'

    https://www.codewars.com/kata/alphabetical-sequence/train/python
    """
    output_list_of_strings = []
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in string:
        number_of_trailing_letters = ALPHABET.find(letter.upper())
        # output_element example: "Eeeee"
# import pdb; pdb.set_trace()
        output_element = letter.upper() + letter.lower()*number_of_trailing_letters
        output_list_of_strings.append(output_element)
    output_string = ",".join(output_list_of_strings)
    return output_string


if __name__ == '__main__':
    print("*"*20)
    print("running doctest...")
    print("*"*20)
    import doctest
    doctest.testmod()
