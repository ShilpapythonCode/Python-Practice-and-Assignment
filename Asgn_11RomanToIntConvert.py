#Given a roman numeral, convert it to an integer

def RomanToInteger(RtoI):
    roman={'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
    integer=0
    for i in range(len(RtoI)):
        value=roman[RtoI[i]]
        if i+1<len(RtoI) and roman[RtoI[i+1]] > value :
            integer-=value
        else:
            integer+=value
    return integer

Rom_Num=input("Enter any Roman Number : ")
print(RomanToInteger(Rom_Num))


