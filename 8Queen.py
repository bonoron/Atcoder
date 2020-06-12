from itertools import permutations
n=int(input())
A=[list(map(int,input().split())) for _ in range(n)]

B=[]
for Q in permutations(range(8)):
    if len(set(i+j for i,j in enumerate(Q)))==8 and len(set(i-j for i,j in enumerate(Q)))==8:
        point=0
        for i in range(n):
           if Q[A[i][0]]==A[i][1]:point +=1
        if point==n:
            B=[["." for _ in range(8)] for _ in range(8)]
            for i,j in enumerate(Q):
                B[i][j]="Q"
            for i in range(8):
                print("".join(B[i]))