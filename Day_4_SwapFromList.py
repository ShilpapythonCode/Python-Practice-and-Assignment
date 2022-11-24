"""1.	Write a program to swap two elements in a list:
Input : List = [3, 2,1, 4], pos1 = 1, pos2 = 3
Output : [1, 2, 3 4]"""

List = [3, 2, 1, 4]
pos1 = 1
pos2 = 3

temp = List[pos1-1]
List[pos1-1]=List[pos2-1]
List[pos2-1]=temp
print(List)

# 2.	Write a program to find second largest number in a list:
#Input: L=[1,2,3,4]
#Output: 3

L=[1, 2, 3, 4]
L.sort()
print(L[-2])

# 3. Write a program to find sum and average of a list:
# Input: L = [10,20,30,40]
# Output : sum = 100 , avg = 25
#SUM
L = [10, 20, 30, 40]
sum=0
for num in L :
    sum=sum+num
print("The Sum of [10, 20, 30, 40] : " + str(sum))

#AVG
list_count=len(L)
print(list_count)
avg=int(sum/list_count)
print("The Avg of [10, 20, 30, 40] : " + str(avg))

