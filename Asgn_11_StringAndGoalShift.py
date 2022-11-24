'''8. Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:
Input: s = "abcde", goal = "abced"
Output: false
'''
str1 = "abcde"
str2 = "deabc"

if (len(str1) != len(str2)):
    print("Second string is not a rotation of first string");
else:
    try:
        str1 = str1 + str1


        if (str1.index(str2)):
            print("Second string is a rotation of first string");
    except ValueError:
        print("Second string is not a rotation of first string");


