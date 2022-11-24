'''6. Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
'''

def isSubString(myList):
    n=len(myList)
    l1=[]

    for i in range(n):
        j = i + 1
        while j<n:
            if (myList[i] in myList[j]) and (myList[i] not in l1):
                l1.append(myList[i])
            j+=1

    return l1
words = ["mass","as","hero","superhero","herochamp"]
words.sort()
print(words)
print(isSubString(words))