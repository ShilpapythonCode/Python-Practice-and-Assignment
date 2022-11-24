'''7. You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:
The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.'''

attendance='PPLLALLP'

def Attendance_Award(atten):
    l1=len(atten)
    a=atten.count('A')
    count = 0
    if a>1:
        return False
    if 'L' in atten:
        ind=atten.index('L')

        for ind in range(ind+3):
            if atten[ind]=='L':
                count+=1
    if count>=3:
        return False
    else:
        return True

print(Attendance_Award(attendance))


