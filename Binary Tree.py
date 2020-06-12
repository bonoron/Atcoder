def binary(node,parent,sibling,depth,root):
    if node!=-1:
        id,left,right=A[node]
        degree=len([i for i in (right,left) if i!=-1])
        if parent==-1:root="root"
        elif degree!=0:root="internal node"
        else:root="leaf"
        B.append([node,parent,sibling,degree,depth,root])
        binary(left,node,right,depth+1,root)
        binary(right,node,left,depth+1,root)


def setHight(H,u):
    h1,h2=0,0
    if A[u][2]!=-1:
        h1=setHight(H,A[u][2])+1
    if A[u][1]!=-1:
        h2=setHight(H,A[u][1])+1
    H[u]=max(h1,h2)
    return H[u]


n=int(input())
A=[list(map(int,input().split())) for i in range(n)]
B,H=[],[0]*n
top=[i for i in range(n)]
for i in range(n):
    for j in (A[i][1],A[i][2]):
        if j!=-1:top.remove(j)
top=top[0]
A=sorted(A)
binary(top,-1,-1,0,"root")
setHight(H,top)
for j,i in enumerate(sorted(B)):
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}"
          .format(i[0],i[1],i[2],i[3],i[4],H[j],i[5]))