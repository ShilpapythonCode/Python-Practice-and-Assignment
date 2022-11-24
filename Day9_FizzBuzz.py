'''answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
Examples:
Input: n = 3
Output: ["1","2","Fizz"]
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
'''


def fizzbuzz(n):

    count=1
    list = []
    for i in range(n):
        if (count%3==0 and count%5==0):
           list.append("FizzBuzz")
        elif count%5==0:
           list.append("Buzz")
        elif count%3==0:
            list.append("Fizz")
        else:
            list.append(str(count))
        count+=1

    print(list)

num=int(input("Please enter a Number :"))
fizzbuzz(num)