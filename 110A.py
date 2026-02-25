num=input().strip()
count =0
for d in num:
    if d=='4' or d=='7':
        count+=1
if count>0 and all(d in '47' for d in str(count)):
    print("YES")
else:
    print("NO")