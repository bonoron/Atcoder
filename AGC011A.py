n,c,k=map(int,input().split())
T=sorted([int(input()) for i in range(n)])+[float("inf")]

start,ans,cnt=T[0],0,0
for i in range(n+1):
    if start+k<T[i] or cnt+1>c:
        ans +=1
        cnt=0
        start=T[i]
    cnt +=1

print(ans)