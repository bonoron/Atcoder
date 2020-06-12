from itertools import product
n=int(input())
c=input()

command=["".join(i) for i in product("ABXY", repeat=2)]
ans=n

for i in command:
    for j in command:
        if i!=j:
            c1=c.replace(i,"L")
            c2=c1.replace(j,"R")
            if ans>len(c2):ans=len(c2)

print(ans)