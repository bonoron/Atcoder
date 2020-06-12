import heapq

inf = 10 ** 9


def dijkstra(a):
    color = ["white" for _ in range(n + 1)]
    D = [inf for _ in range(n + 1)]
    P =[-1 for _ in range(n+1)]

    P[a]=-1
    D[a] = 0
    color[a] = "gray"
    queue = [[0, a]]
    heapq.heapify(queue)

    while len(queue) > 0:
        u = heapq.heappop(queue)[1]
        if color[u] == "black": continue
        color[u] = "black"

        V = [[i, j] for i, j in M[u] if color[j] != "black"]
        if len(V) > 0:
            for i, j in V:
                if D[u] + i < D[j]:
                    D[j] = D[u] + i
                    color[j] = "gray"
                    P[j]=u
                    heapq.heappush(queue, [D[j], j])

    return P,D


n,m=map(int,input().split())
AB=[list(map(int,input().split())) for _ in range(m)]
M=[[] for _ in range(n+1)]
for a,b in AB:
    M[a].append([1,b])
    M[b].append([1,a])
P,D=dijkstra(1)
if inf not in D[1:]:
    print("Yes")
    for i in P[2:]:
        print(i)
else:print("No")