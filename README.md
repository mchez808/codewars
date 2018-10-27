# codewars

## 7 kyu

### [Alphabetical Sequence](https://www.codewars.com/kata/alphabetical-sequence/train/python)

In this kata you will be given a random string of letters and tasked with
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


## 8 kyu

### [Invert values](https://www.codewars.com/kata/invert-values/train/python)

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.


### [Pillars](https://www.codewars.com/kata/pillars/train/python)

There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Your function accepts three arguments:

1. number of pillars (≥ 1);
2. distance between pillars (10 - 30 meters);
3. width of the pillar (10 - 50 centimeters).
Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar).

(assertions also added)


### [Super Duper Easy](https://www.codewars.com/kata/super-duper-easy/train/python)

Make a function that returns the value multiplied by 50 and increased by 6.
If the value entered is a string it should return "Error".
