# WAP to convert Integer to Binary

def IntToBinary(num):
    BinStr=""
    str1 = ""

    while num>1:
        rem=num%2
        BinStr+=str(rem)
        num=int(num/2)
    BinStr += str(num)
    i=len(BinStr)-1

    while i>-1:
        str1+=BinStr[i]
        i-=1

    return str1

num1=int(input("Please enter the number : "))
print(IntToBinary(num1))
