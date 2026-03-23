t=int(input())
for _ in range(t):
    s=input()
    count=0
    if s[0]=='a':
        count+=1
    if s[1]=='b':
        count+=1
    if s[2]=='c':
        count+=1
    if count>=1:
        print("YES")
    else:
        print("NO")