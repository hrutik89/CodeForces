n=int(input())
t=input().strip()
count=0
for i in range(n-1):
    if t[i]==t[i+1]:
        count+=1
print(count)