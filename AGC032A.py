n=int(input())
B=list(map(int,input().split()))
A=[]
for i in range(n):
    for j in reversed(range(len(B))):
        if B[j]==j+1:
            A.append(B.pop(j))
            break
    else:
        print(-1)
        exit()
print(*reversed(A),sep="\n")