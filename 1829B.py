t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    maxs=0
    for i in arr:
        if i ==0:
            count+=1
            maxs=max(count,maxs)
        else:
            count =0
    print(maxs)