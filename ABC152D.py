n=int(input())
A=[[0 for i in range(9)] for j in range(9)]

for i in range(1,n+1):
    if i%10!=0:
        num=str(i)
        A[int(num[0])-1][int(num[-1])-1] +=1

cnt=0
for i in range(9):
    for j in range(9):
        cnt +=A[i][j]*A[j][i]

print(cnt)