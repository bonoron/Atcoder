n=int(input())
A=[int(input()) for _ in range(n)]+[0]

cnt=0
for i in range(n):
    cnt +=A[i]//2
    if A[i+1]!=0:
        cnt +=A[i]%2
        A[i+1] -=A[i]%2

print(cnt)