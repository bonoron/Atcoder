n,m=map(int,input().split())
X=sorted(list(map(int,input().split())))

A=[]
for i in range(m-1):
    A.append(abs(X[i]-X[i+1]))

A.sort()
ans=0
for i in range(m-n):
    ans +=A[i]
print(ans)