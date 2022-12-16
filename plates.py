s = "he11o"
for j in s:
    if (j.isdigit() and j !=0):
        a = s.index(j)
        if s[a+1:].isdigit():
            print("yasss")
    else:
        print("mehhh")
