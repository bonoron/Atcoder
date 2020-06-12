n,a,b=map(int,input().split())
X=list(map(int,input().split()))
cnt=0
for i in range(n-1):
    dis=X[i+1]-X[i]
    if dis*a>b:cnt +=b
    else:cnt +=dis*a
print(cnt)