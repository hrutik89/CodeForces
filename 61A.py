a=input()
b=input()
for i in range(len(a)):
    if int(a[i]) == int(b[i]):
        print(0,end="")
    else:
        print(1,end="")