# 8 kyu

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

