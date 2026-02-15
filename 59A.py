s=input()
up=0
low=0
for c in s:
    if(c.isupper()):
        up+=1
    else:
        low+=1
if(low>up):
    print(s.lower())
elif(low==up):
    print(s.lower())
else:
    print(s.upper())