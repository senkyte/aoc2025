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