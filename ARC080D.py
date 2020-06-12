h,w=map(int,input().split())
n=int(input())
A=list(map(int,input().split()))
MAP=[[0 for i in range(w)] for j in range(h)]
s,num=0,1
for i in range(h):
    if i%2==0:add=[k for k in range(w)]
    else:add=[k for k in reversed(range(w))]
    for j in add:
        MAP[i][j]=num
        A[s] -=1
        if A[s]==0:
            s +=1
            num +=1

for i in range(h):print(*MAP[i])