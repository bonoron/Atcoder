n,x=map(int,input().split())
A=list(map(int,input().split()))

cnt=0
for i in range(n-1):
    point=A[i]+A[i+1]
    cnt +=max(0,point-x)
    if point>x:A[i+1]=max(0,A[i+1]-(point-x))

print(cnt)