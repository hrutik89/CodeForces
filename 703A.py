t=int(input())
counta=0
countb=0
for _ in range(t):
    a,b=map(int,input().split())
    if a>b:
        counta+=1
    elif b>a:
        countb+=1
if counta>countb:
    print("Mishka")
elif counta==countb:
    print("Friendship is magic!^^")
else:
    print("Chris")