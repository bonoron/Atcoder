import re
n=int(input())
A=[]
for i in range(n):
    B=["."]*n
    for x,y in [list(map(int,input().split())) for k in range(int(input()))]:
        B[x-1]=str(y)
    A.append("".join(B))
ans=0
for i in range(2**n):
    num=format(i,"b").zfill(n)
    cnt,flag=0,1
    for k,j in enumerate(num):
        result=re.search(r"".join(A[k]),num)
        if result is not None and j=="1":
            cnt +=1
        elif (result is not None and j=="0") or (result is None and j=="1"):
            flag=0
            break
    if flag:ans=max(ans,cnt)
print(ans)