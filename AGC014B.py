n,m=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(m)]

Tree=[[] for _ in range(n+1)]
for a,b in AB:
    Tree[a].append(b)
    Tree[b].append(a)

for i in range(1,n+1):
    if len(Tree[i])%2==0:continue
    else:
        print("NO")
        exit()
print("YES")