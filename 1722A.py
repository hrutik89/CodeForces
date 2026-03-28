t=int(input())
c="Timur"
for _ in range(t):
    i=int(input())
    s=input()
    if sorted(s)==sorted(c):
        print("YES")
    else:
        print("NO")