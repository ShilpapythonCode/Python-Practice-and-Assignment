"""5 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]"""

nums = [2 , 7 , 11 , 15]
target = 17
i=0
j=1
while i <= len(nums)-1:
     while j <= len(nums)-1:
        sum = nums[i] + nums[j]
        if sum==target:
            print("[" + str(i)+ "," +str(j)+"]")
            break
        j=j+1
     i=i+1
     j=i+1

'''6 Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Input: nums = [1,2,3,1]
Output: true'''


nums = [1,2,3,4]
i=0
j=1
while i <= len(nums)-1:
     while j <= len(nums)-1:
        if nums[i]==nums[j]:
            print("True")
            break
        j=j+1
     i=i+1
     j=i+1

if i==len(nums):
    print("False")

"""7 Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
Input: nums = [1,2]
Output: 2
Explanation : The 3rd distinct maximum doesn’t exist so 2 is returned."""

nums = [1,22,8,98,98,11,98]
result = []
for i in nums:
    if i not in result:
        result.append(i)

result=sorted(result)

print(result[-3])

'''Bonus question:
Print negative number starting from -10 to -100 skipping the odd numbers.
Note: As we discussed today, range object doesn’t generate negative integers by default so we need to explicitly specify the range values using start, step or stop'''

for i in range(-10, -100, -2):
    print(i, end= " ")
print()


