t=int(input())
for _ in range(t):
    res=0
    n=int(input())
    l=list(map(int,input().split()))
    if l[0]==l[1]:
        res=l[0]
    else:
        if l[0]==l[2]:
            res=l[0]
        else:
            res=l[1]
    for i in range(n):
        if l[i]!=res:
            print(i+1)
            break