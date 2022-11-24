'''Take the input from the user for the length field.
Min. length should be 24, any input less than 24 should throw an error message stating the error as  ‘Length value should be  >=24’
'''
class Error(Exception):
    pass

class SmallValueError(Error):
    pass
number=24

try:
    s1=input("Please enter character Min. 24 : ")
    l=len(s1)
    if l <= 24:
        raise SmallValueError
except SmallValueError:
    print("Length value should be  >=24, try again!")
    print()
