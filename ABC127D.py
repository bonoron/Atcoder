from collections import deque
n,m=map(int,input().split())
A=sorted(list(map(int,input().split())))
BC=sorted([list(map(int,input().split())) for i in range(m)],key=lambda x:x[1])
A=deque(A)
for b,c in BC[::-1]:
    for i in range(b):
        if A[0]<c:
            A.append(c)
            A.popleft()
        else:break
print(sum(A))