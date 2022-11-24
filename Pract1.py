# WAP to display O/p: "ShYa"

full_name="Shilpa Yande"
in_name=full_name.split(" ")
print(in_name)

ch=""
for i in in_name:
    ch+=str(i[slice(0,2)])
    #print(i[slice(0,2)])

print(ch)