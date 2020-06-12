k,t=map(int,input().split())
A=sorted(list(map(int,input().split())), key=lambda x: -x)
while len(A)!=1:
    A[0] -=A.pop(1)
    A=sorted(A, key=lambda x: -x)
print(A[0]-1 if A[0]!=0 else 0)