'''3. Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3
'''

def majorityElement(nums,n):
    maxCount=0
    index=-1
    for prev in range(n):
        count=0
        for next in range(n):
            if nums[prev]==nums[next]:
                count+=1
        if(count>maxCount):
            maxCount=count
            index=prev

    if (maxCount > n // 2):
        print("Majority element is ", nums[index])

    else:
        print("Majority Element does not exist")

nums=[3,2,3,1,9,8,3,3,3]
n=len(nums)
majorityElement(nums,n)