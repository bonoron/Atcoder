B=list(map(int,input().split()))
B=sorted([(B[i],i) for i in range(10)])
n=int(input())
A=[int(input()) for _ in range(n)]
length=len(str(max(A)))
C=[(str(A[i]).zfill(length),i) for i in range(n)]

D=[]
for i in range(n):
    num=list(C[i][0])
    for j in range(length):
        num[j]=str(B[int(num[j])][1])
    D.append((int("".join(num)),C[i][1]))

D=sorted(D)
for i,j in D:
    print(A[j])