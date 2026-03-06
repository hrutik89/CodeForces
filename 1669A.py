n=int(input())
for _ in range(n):
    t=int(input())
    if t>=1900:
        print("Division 1")
    elif 1600<=t<=1899:
        print("Division 2")
    elif 1400<=t<=1599:
        print("Division 3")
    elif t<=1399:
        print("Division 4")