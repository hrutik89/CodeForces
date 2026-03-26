t=int(input())
for _ in range(t):
    n=input()
    res=[]
    for i in range(len(n)):
        if(n[i]!='0'):
            res.append(n[i]+'0'*(len(n)-i-1))
    print(len(res))
    print(*res)