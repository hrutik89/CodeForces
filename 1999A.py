n=int(input())
for _ in range(n):
    sum=0
    digit=0
    t=int(input())
    while(t!=0):
        digit=int(t%10)
        sum+=digit
        t=int(t/10)
    print(sum)