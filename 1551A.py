t=int(input())
for _ in range(t):
    n=int(input())
    a=n//3
    b=n%3
    if(b==2):
        print(a,a+1)
    else:
        print(b+a,a)