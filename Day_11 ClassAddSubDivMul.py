# WAP to perform Addition, Substraction, Division, Multiplication

class Fraction_Calculator:

    def __init__(self,num,den):
        self.num= num
        self.den= den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        temp_num=self.num * other.den+ other.num * self.den
        temp_den=self.den * other.den
        return f"{temp_num}/{temp_den}"

    def __sub__(self, other):
        temp_num=self.num * other.den - other.num * self.den
        temp_den= self.den * other.den
        return f"{temp_num}/ {temp_den}"

    def __mul__(self, other):
        temp_num=self.num * other.num
        temp_den= self.den * other.den
        return f"{temp_num}/{temp_den}"

    def __truediv__(self, other):
        temp_num=self.num*other.den
        temp_den=self.den * other.num
        return f"{temp_num}/{temp_den}"



x=Fraction_Calculator(2,3)
y=Fraction_Calculator(3,3)
print(x)
print(y)
print("Addition for Fraction : " + str(x+y))
print("Substraction for Fraction : " + str(x-y))
print("Multiplication for Fraction : " + str(x*y))
print("Division for Fraction : " + str(x/y))
