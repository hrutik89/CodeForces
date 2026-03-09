n = int(input())
a = list(map(int, input().split()))

maxi = max(a)
ans = 0

for i in a:
    ans += maxi - i

print(ans)