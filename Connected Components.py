from collections import deque


def CC():
    id=0
    color=["white" for i in range(n)]
    for j in range(n):
        if color[j]=="white":
            color[j]="gray"
            queue=deque([j])

            while len(queue)!=0:
                u=queue.popleft()
                for i in M[u]:
                    if color[i]=="white":
                        color[i]="gray"
                        queue.append(i)
                color[u]=str(id)
            id +=1

    return color


n,m=map(int,input().split())
M=[[] for i in range(n)]
for i in range(m):
    p,q=map(int,input().split())
    M[p].append(q)
    M[q].append(p)

color=CC()

for i in range(int(input())):
    a,b=map(int,input().split())
    print("yes" if color[a]==color[b] else "no")