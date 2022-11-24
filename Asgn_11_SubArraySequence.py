'''9. Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.
Return true if these subarrays exist, and false otherwise.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input: nums = [4,2,4]
Output: true
Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.
Example 2:
Input: nums = [1,2,3,4,5]
Output: false
Explanation: No two sub-arrays of size 2 have the same sum.
'''

nums=[4,2,4]
length1=len(nums)
def SubArraySequence(nums,length1):
    i=0
    j=i+1
    temp=0
    while j<length1-1:
        temp=nums[i]+nums[j]
        i += 1
        j = i + 1
    if temp == (nums[i] + nums[j]):
        return True
    else:
        return False

print(SubArraySequence(nums, length1))





