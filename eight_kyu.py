# 8 kyu
# There are pillars near the road. The distance between the pillars is the same
# and the width of the pillars is the same.
# Your function accepts three arguments:
    # number of pillars (≥ 1);
    # distance between pillars (10 - 30 meters);
    # width of the column (10 - 50 centimeters).

import doctest

def pillars(num_pill, dist, width):
    """Calculate the distance between the first and
    the last pillar in centimeters (without the width of the first and last pillar).

    >>> pillars(1, 10, 10)
    0

    >>> pillars(2, 20, 25)
    2000

    >>> pillars(11, 15, 30)
    15270

    """
    if num_pill <= 1:
        return 0
    return dist*100 * (num_pill - 1) + width * (num_pill - 2)

doctest.testmod()
