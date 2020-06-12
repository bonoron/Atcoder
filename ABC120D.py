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

    def Count(self,x):
        return -self.root[self.Find_Root(x)]

    def members(self,x):
        root=self.Find_Root(x)
        return [i for i in range(self.n) if self.Find_Root(i)==root]

    def address(self):
        return[i for i,j in enumerate(self.root) if j<0]

    def group_members(self):
        return {i:self.members(i) for i in self.address()}

    def size(self,x):
        return -self.root[self.Find_Root(x)]


n,m=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(m)]
UnionFind=UnionFind(n)
count=[n*(n-1)//2]

for a,b in AB[::-1]:
    if UnionFind.isSameGroup(a-1,b-1):
        count.append(count[-1])
    else:
        s,t=UnionFind.size(a-1),UnionFind.size(b-1)
        count.append(count[-1]-s*t)
    UnionFind.Unite(a-1,b-1)

for i in count[::-1][1:]:
    print(i)