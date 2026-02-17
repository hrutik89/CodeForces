x,k=map(int,input().split())
for _ in range(k):
    if(x%10!=0):
        x-=1
    elif(x%10==0):
        x/=10
print(int(x))    
