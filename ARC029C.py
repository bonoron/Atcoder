import heapq


def prim(v,m):
    inf=10**12
    M=[[] for _ in range(v+1)]
    color=["white" for _ in range(v+1)]
    D=[inf for _ in range(v+1)]

    for i in range(v):
        num=int(input())
        M[0].append((num,i+1))
        M[i+1].append((num,0))

    D[0]=0

    for i in range(m):
        s,t,w=map(int,input().split())
        M[s].append((w,t))
        M[t].append((w,s))

    H=[(0,0)]
    heapq.heapify(H)

    cnt=0
    while len(H)>0:
        cost,u=heapq.heappop(H)

        if color[u]=="black":continue
        color[u]="black"
        cnt +=1

        for i,j in M[u]:
            if color[j]!="black" and D[j]>i:
                D[j]=i
                color[j]="gray"
                heapq.heappush(H,(i,j))

        if cnt==v+1:break

    return D


n,m=map(int,input().split())
ans=prim(n,m)
print(sum(ans))