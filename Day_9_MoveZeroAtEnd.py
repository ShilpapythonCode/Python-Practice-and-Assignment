'''4. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements
Note that you must do this in-place without making a copy of the array.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0] '''

def moveZeroEnd(nums,n):
    count=0

    for i in range(n):
        if(nums[i]!=0):
            nums[count]=nums[i]
            count+=1
    while count<n:
        nums[count]=0
        count+=1

nums=[0,1,0,3,12,0,0,3,7,0,8,9]
n=len(nums)
moveZeroEnd(nums,n)

print(nums)