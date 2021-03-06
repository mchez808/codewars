# 8 kyu

def invert(inputlist):
    """Given a set of numbers, return the additive inverse of each.
    Each positive becomes negatives, and the negatives become positives.

        invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
        invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
        invert([]) == []
    You can assume that all values are integers. Do not mutate the input array/list.

    https://www.codewars.com/kata/invert-values/train/python
    """
    outputlist = []
    for n in inputlist:
        outputlist.append(-1*n)
    return outputlist


def problem(a):
    """Make a function that returns the value multiplied by 50 and increased by 6.
    If the value entered is a string it should return "Error".

    https://www.codewars.com/kata/super-duper-easy/train/python
    """
    if(isinstance(a, str)):
        return "Error"
    return a*50 + 6


def pillars(num_pill, dist, width):
    # There are pillars near the road. The distance between the pillars is the same
    # and the width of the pillars is the same.
    # Your function accepts three arguments:
    # number of pillars (≥ 1);
    # distance between pillars (10 - 30 meters);
    # width of the column (10 - 50 centimeters).
    """Calculate the distance between the first and
        the last pillar in centimeters (without the width of the first and last pillar).

    https://www.codewars.com/kata/pillars/train/python
    """
    if num_pill <= 1:
        return 0
    return dist*100 * (num_pill - 1) + width * (num_pill - 2)


def abbrevName(name):
    """
    Write a function to convert a name into initials.
    This kata strictly takes two words with one space in between them.
    The output should be two capital letters with a dot seperating them.
    It should look like this:

    >>> abbrevName("Sam Harris")
    'S.H'

    >>> abbrevName("Patrick Feeney")
    'P.F'

    https://www.codewars.com/kata/abbreviate-a-two-word-name/train/python
    """
    return ".".join([name.split()[0][0], name.split()[1][0]]).upper()


def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    You were camping with your friends far away from home, but when it's time to
    go back, you realize that you fuel is running out and the nearest pump is
    50 miles away! You know that on average, your car runs on about 25 miles per
    gallon. There are 2 gallons left. Considering these factors, write a
    function that tells you if it is possible to get to the pump or not.
    Function should return true if it is possible and false if not.

    https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
    """
    return distance_to_pump <= mpg*fuel_left
