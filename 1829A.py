t=int(input())
for _ in range(t):
    n=input()
    count =0
    c="codeforces"
    for i in range(10):
        if n[i]!=c[i]:
            count+=1
    print(count)