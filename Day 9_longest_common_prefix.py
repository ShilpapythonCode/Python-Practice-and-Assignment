'''1. Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''
strs = ["flower", "flow", "flight"]
def lcd(strs):

    if len(strs)==0:
        return ""
    if len(strs)==1:
        return first_val

    first_val = strs[0]
    first_len = len(strs[0])

    for i in strs[1:]:
        while first_val!=i[0:first_len]:
            first_val=first_val[0:(first_len-1)]
            first_len-=1
            if first_len==0:
                return " "

    return first_val

print(lcd(strs))

