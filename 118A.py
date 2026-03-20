t=input().lower()
vowels="aeiouy"
ret=""
for s in t:
    if s not in vowels:
         ret+="."+s
print(ret)