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

    def size(self,x):
        return -self.root[self.Find_Root(x)]

    def members(self,x):
        root=self.Find_Root(x)
        return [i for i in range(self.n) if self.Find_Root(i)==root]

    def address(self):
        return[i for i,j in enumerate(self.root) if j<0]

    def group_members(self):
        return {i:self.members(i) for i in self.address()}


n,m=map(int,input().split())
B=[n-i for i in range(n)]+[int(input()) for _ in range(m)]
UnionFind=UnionFind(n+1)

for i in B[::-1]:
    if not UnionFind.isSameGroup(0,i):
        print(i)
        UnionFind.Unite(0,i)