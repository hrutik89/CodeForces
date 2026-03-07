t=int(input())
sum=0
for _ in range(t):
    
    a=input()
    if(a=="Tetrahedron"):
        sum+=4
    if(a=="Cube"):
        sum+=6
    if(a=="Octahedron"):
        sum+=8
    if(a=="Dodecahedron"):
        sum+=12
    if(a=="Icosahedron"):
        sum+=20
print(sum)