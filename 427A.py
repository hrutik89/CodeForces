n=int(input())
a=list(map(int,input().split()))
count = 0
untreated=0
for i in a:
    if i>0:
        count+=i
    else:
        if count>0:
            count-=1
        else:
            untreated+=1
print(untreated)