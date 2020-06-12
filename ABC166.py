N=int(input())
A=list(map(int,input().split()))
S,D=[0]*N,[0]*N

for i in range(N):
    if A[i]+i<N:S[A[i]+i] +=1
    if i-A[i]>0:D[i-A[i]] += 1

ans=0
for l in range(N):
    ans += S[l]*D[l]

print(ans)