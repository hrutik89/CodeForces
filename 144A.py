n=int(input())
a=list(map(int,input().split()))
count=0
maxi =max(a)
mini=min(a)
max_i=a.index(maxi)
min_i=len(a)-1-a[::-1].index(mini)
moves=max_i+(n-1-min_i)
if max_i>min_i:
    moves-=1
print(moves)