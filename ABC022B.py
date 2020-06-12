A=[int(input()) for i in range(int(input()))]
kind={}
cnt=0
for i in range(len(A)):
    if A[i] not in kind:kind[A[i]]=1
    else:cnt +=1
print(cnt)