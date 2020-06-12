n=int(input())+1
A=[0]+list(map(int,input().split()))
Heap=[]
for i in range(1,n):
    parent,right,left=i//2,i*2,i*2+1
    right=A[right] if right<n else 0
    left=A[left] if left<n else 0
    Heap.append([i,A[i],A[parent],right,left])

for i in range(n-1):
    node,key,parent,left,right=Heap[i]
    print("node {}: key = {}, ".format(node,key), end="")
    if parent!=0:print("parent key = {}, ".format(parent), end="")
    if left!=0:print("left key = {}, ".format(left), end="")
    if right!=0:print("right key = {}, ".format(right), end="")
    print()