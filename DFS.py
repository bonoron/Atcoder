def DFS(start):
    global timer
    color[start]="gray"
    time[start][1]=timer
    timer +=1
    for i in range(n):
        if M[start][i] and color[i]=="white":
            DFS(i)
    color[start]="black"
    time[start][2]=timer
    timer +=1


n=int(input())
A=[list(map(int,input().split())) for i in range(n)]
M=[[0 for i in range(n)] for j in range(n)]
time=[[i+1,0,0] for i in range(n)]
color=["white" for i in range(n)]

for i in range(n):
    for j in A[i][2:]:
        M[i][j-1]=1

timer=1
for i in range(n):
    if color[i]=="white":
        DFS(i)

for i in range(n):
    print(*time[i])