t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    count=0
    if a%b==0:
        print(count)
    else:
        while(a%b!=0):
            a+=1
            count+=1
        print(count)