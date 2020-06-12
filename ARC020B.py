from collections import Counter
n,c=map(int,input().split())
A=[int(input()) for _ in range(n)]
B=Counter(A[::2]).most_common(2)
C=Counter(A[1::2]).most_common(2)
if len(B)==1:B.append([0,0])
if len(C)==1:C.append([0,0])
if B[0][0]==C[0][0]:
    print(max((n-B[1][1]-C[0][1])*c,
              (n-B[0][1]-C[1][1])*c))
else:print((n-B[0][1]-C[0][1])*c)