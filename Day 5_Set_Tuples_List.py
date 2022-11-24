# Return a set of common elements present in Set A and B:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

set1= {10,20,30,40,50}
set2= {30,40,50,60,70}
list1=[1,2,3,4,5]
print(len(list1))
print(sorted(set1|set2))

print(sorted(set1&set2))

#Write a Python program to find the length of a set.
set_len=len(set1)
print(set_len)

#Create an empty set and add the below elements to it:
# 10,20,30,40
empty_set=set()
empty_set.add(10)
empty_set.add(20)
empty_set.add(30)
empty_set.add(40)
print(sorted(empty_set))

# Remove all duplicates words from a given sentence
# String = “ You cannot end a sentence with because because because is a conjunction.”
String = " You cannot conjunction end a sentence with because a because because is a conjunction end."
print(' '.join(set(String.split())))   #output will be same

l = String.split()
k = []
for i in l:

    if (String.count(i) >= 1 and (i not in k)):
        k.append(i)
print(' '.join(k))



