n,m=map(int,input().split())
A=[[i,list(map(int,input().split()))] for i in range(m)]
A.sort(key=lambda x:x[1][1])
B={}
for x,y in A:
    if y[0] not in B:
        B[y[0]]=1
        y[1]=1
    else:
        B[y[0]] +=1
        y[1]=B[y[0]]

for i in sorted(A,key=lambda x:x[0]):
    print(str(i[1][0]).zfill(6)+str(i[1][1]).zfill(6))