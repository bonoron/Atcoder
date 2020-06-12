n=int(input())
A=sorted([[int(input()),i] for i,j in enumerate(range(n))])
cnt,num=0,A[0][0]
B=[]

for i in range(n):
    if A[i][0]==num:
        B +=[[cnt,A[i][1]]]
    else:
        cnt +=1
        B +=[[cnt,A[i][1]]]
        num=A[i][0]

B.sort(key=lambda x:x[1])
for i in range(n):
    print(B[i][0])