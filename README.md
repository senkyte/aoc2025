Some documentation i guess, see if i beat all 12 days lol

Day 1
Simple challenge, a rotation lock which starts at 50. Every time you rotate until 0, it resets back to 99, and 99 back to 0. 
The question wants how many times the position ended at 0, then everytime it even touches 0 during a rotation
Solution:
1. Read the file line by line. Idenfiy the direction(line[i]). Identify the magnitude (line[1:]).
2. Apply the rotation to the starting position of 50. Implemented using a while loop. Floor the postion by 100 to calculate the number of complete rotations (number of 0s), as well as modulo the position by 100 to remove complete rotations.
3. Add a counter to count the number of complete rotations, and you have the solution!

Day 2
Find out if a range of numbers are composed of substrings. 
Solution (part 1):
1. If length of number is odd, continue since invalid ids contain 2 substrings
2. Split the string into 2 and check.
Solution (part 2):
1. Using an algorithm, a string S made of substring T, S+S[1:-1] will contain S.
2. Apply this logic, remove the even length checker.
badabing badaboom 

Day 3
Find largest number comparised of n digits in a string of digits
Solution:
1. Using an greedy algorithm, check for every possible valid digit in a range, so on
thats... it. sum it up and you got the answer

Day 4
WOW. Surprisingly easier than day 3. 
Find all valid @. Condition: There must be < 4 @ around a 3x3 radius. For the second part, you are allowed to remove valids and iterate again
Solution:
1. Check 3x3 for every @. If valid, add and remove
2. Loop until there are no longer valid @.

Day 5 
Given a list of ranges, check the number of valid ints. 
Part 1 Solution:
1. Read all of the ranges. Store it into a list as a list [lower, upper]
2. Read all of the values needed to be checked. Iterate through the list and check with a simple inequality check.
3. Record the number of valid ones.
Part 2 Solution:
1. Create a new list merged. We now just gotta merge all the ranges then find the max number of valid ids
2. This code runs under the assumption that the id ranges get bigger and bigger ONLY. 
3. Check if the ranges are within the current range, if so overwrite. Else if not in current range, we can just append it to the merge list and replace the current range with the latest range.
4. Calculate the total number with basic math.