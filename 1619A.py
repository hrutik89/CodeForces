t=int(input())
for _ in range(t):
    s=input()
    if len(s) % 2!=0:
        print("NO")
    else:
        i = len(s)//2
        if s[:i] == s[i:]:
            print("YES")
        else:
            print("NO")