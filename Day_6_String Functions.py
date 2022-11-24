# 1 Given a string s consisting of words and spaces, return the length of the last word in the string. Make sure your program works for other values of  ‘s’ as well
# Input: s = "   fly me   to   the moon  "
# Output: 4

print("Hello")


def length(str):
    # Split by space and converting String to list
    lis = list(str.strip().split(" "))
    return len(lis[2])


# Driver code
str = "   fly me   to   the moon  "
res = " ".join(str.strip().split())  # remove additional space from string
print("The length of last word is", length(res))

# 2 Find the frequency of occurrence of each character in the below string and display the out put as shown: Make sure your program works for other values of  ‘s’ as well
# Input: s = “aaabbcdddee”
# Output: a3b2c1d3e2

s = "aaabbcdddee"
print("The input string is:", s)
mySet = set(s)

mySet=sorted(mySet) #Soting for output sequence

str=""
for i in mySet:
    countOfChar = 0
    for char in s:
        if char == i:
            countOfChar += 1
    str = str + "{}{}".format(i, countOfChar)

print(str)

# 3 Given a string s, return true if it is a palindrome, or false otherwise. Make sure your program works for other values of  ‘s’ as well
# Example Input: s = "race a car"
# Output: false

def isPalindrome(s):
    x = list(s)
    y = []
    y.extend(x)
    x.reverse()
    if (x == y):
        return True
    return False


# Driver Code
s = "rac a car"
ans = isPalindrome(s)

if ans:
    print("Yes")

else:
    print("No")

#4 Given two strings s and t, return true if t is an anagram of s, and false otherwise. Make sure your program works for other values of  ‘s’ as well
#Input: s = "anagram", t = "nagaram"
#Output: true

# function to check if two strings are
# anagram or not
def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

    # driver code
s1 = "anagram"
s2 = "nagaram"
check(s1, s2)

print(s2[::-1])  # Reversea string