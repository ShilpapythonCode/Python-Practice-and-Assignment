#6. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

str='rbc'
str1='aetberc'

def string_subsequence(str, str1):
    i=0
    while i<len(str):
        if str[i] not in str1:
            return False
        i+=1
    return True
print(string_subsequence(str, str1))

