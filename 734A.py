n=int(input())
s=input()
ac =0
dc =0
for c in s:
    if c=="A":
        ac+=1
    else:
        dc+=1
if(ac>dc):
    print("Anton")
elif(ac==dc):
    print("Friendship")
else:
    print("Danik")