# 6 kyu

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
