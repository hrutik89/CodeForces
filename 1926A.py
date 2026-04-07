t=int(input())
for _ in range(t):
    s=input()
    counta=0
    countb=0
    for c in s:
        if c=='A':
            counta+=1
        else:
            countb+=1
    if counta<countb:
        print("B")
    else:
        print("A")