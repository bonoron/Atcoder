n,k=map(int,input().split())
AB=sorted([list(map(int,input().split())) for i in range(n)])
dic={}
C=[0]
for i in range(n):
    C.append(C[-1]+AB[i][1])
for i in range(n):
    if C[i]<k<=C[i+1]:
        print(AB[i][0])
        exit()