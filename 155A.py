t=int(input())
a=list(map(int,input().split()))
count=0
maxi=a[0]
mini=a[0]
for i in range(1,t):
    if a[i]>maxi:
        count+=1
        maxi=a[i]
    elif a[i]<mini:
        count+=1
        mini=a[i]
print(count)