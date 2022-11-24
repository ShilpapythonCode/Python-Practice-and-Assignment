'''Input: emails = ["test.email+alex@verve.com","test.e.mail+bob.cathy@verve.com","testemail+david@ver.ve.com"]
Output: 2
Explanation: "testemail@verve.com" and "testemail@ver.ve.com" actually receive mails.'''

emails = ["test.email+alex@verve.com","test.e.mail+bob.cathy@verve.com","testemail+david@ver.ve.com"]
def forwordEmails(em):
    li=[]

    emailsplit=[]
    for i in em:
        str1 = ""
        length1=len(i)
        emailsplit = i.split("@")
        for j in emailsplit[0]:
            if j=='+':
                break
            elif j!='.':
                str1+=j

        str1+="@"
        str1+=str(emailsplit[1])
        if str1 not in li:
            li.append(str1)
    print("These email Id's " + str(li) +  " actually receives the mail ")
print(emails)
forwordEmails(emails)