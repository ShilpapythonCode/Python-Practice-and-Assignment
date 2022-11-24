#Print and observe the output of the following:
# 07-11-2022

x= 5 + int("7")
print (x)

y= str(5)+'5'
print(y)

#z= int("3.4")
#print(z)
z= int(float("3.4"))
print(z)

#Join the following string and replace the “,” with “:”
s = "the,quick,brown,fooox"
print(s.isalpha())
s1=s.replace(",",":")
print(s1)

#Capitalize first letter of each word separated by “:” in the above example.
split_str = s1.split(':')
result = []
for word in split_str:
    result.append(word.capitalize())
print(result)

#Capitalize first letter of each word separated by “:” in the above example.
print(s1.title())
print(s.isalpha())
print(s1.isdigit())

y="hello"
print(y.isalpha())
print(y.isdigit())
print(s.count("o"))

