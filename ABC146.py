import sys
sys.setrecursionlimit(100000)


def RootedTree(node,parent,root,add):
    A.append([node,parent,root,add])
    for root_num,num in root:
        RootedTree(root_num,node,tree[root_num],num)


n=int(input())
AB=[list(map(int,input().split()))+[i+1] for i in range(n-1)]
A=[]
tree=[[] for i in range(n+1)]
for a,b,c in AB:
    tree[a] +=[[b,c]]

RootedTree(1,0,tree[1],0)
ans=[0]*n
for node,parent,root,num in A:
    flag=0
    for i,j in enumerate(root):
        if ans[num]==i+1:flag=1
        if flag:
            ans[j[1]]=i+2
            continue
        ans[j[1]]=i+1

print(max(ans))
for i in range(1,n):print(ans[i])