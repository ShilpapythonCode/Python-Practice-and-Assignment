#WAP to for integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def ConvertNumToExcelCol(num):
    quo = num // 26
    rem= num % 26
    str1=''
    if num < 26:
        str1=alpha[num - 1]
        return str1
    else:
            if rem == 0:
                if quo == 1:
                    str1= alpha[rem - 1]
                    return str1
                else:
                    str1= ConvertNumToExcelCol(quo - 1) + alpha[rem - 1]
                    return str1
            else:
                str1=ConvertNumToExcelCol(quo) + alpha[rem - 1]
                return str1

num=int(input("Enter a number to convert into column of Excel Sheet : "))
print(ConvertNumToExcelCol(num))

