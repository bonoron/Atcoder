class UnionFind():
    def __init__(self,n):
        self.n=n
        self.root=[-1]*n
        self.rank=[-1]*n

    def Find_Root(self,x):
        if self.root[x]<0:return x
        else:
            self.root[x]=self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self,x,y):
        x=self.Find_Root(x)
        y=self.Find_Root(y)

        if x==y:return
        elif self.rank[x]>self.rank[y]:
            self.root[x] +=self.root[y]
            self.root[y]=x
        else:
            self.root[y] +=self.root[x]
            self.root[x]=y
            if self.rank[x]==self.rank[y]:
                self.rank[y] +=1

    def isSameGroup(self,x,y):
        return self.Find_Root(x)==self.Find_Root(y)

    def members(self,x):
        root=self.Find_Root(x)
        return [i for i in range(self.n) if self.Find_Root(i)==root]

    def address(self):
        return[i for i,j in enumerate(self.root) if j<0]

    def group_members(self):
        return {i:self.members(i) for i in self.address()}

    def size(self,x):
        return -self.root[self.Find_Root(x)]


n,m,k=map(int,input().split())
AB=[list(map(int,input().split())) for _ in range(m)]
CD=[list(map(int,input().split())) for _ in range(k)]

A=UnionFind(n+1)
C=[[] for _ in range(n+1)]
D=[[] for _ in range(n+1)]

for a,b in AB:
    A.Unite(a,b)
    C[a] +=[b]
    C[b] +=[a]

for c,d in CD:
    if A.isSameGroup(c,d):
        D[c] +=[d]
        D[d] +=[c]

ans=[]
for i in range(1,n+1):
    ans +=[A.size(i)-len(C[i])-len(D[i])-1]

print(*ans)