n=int(input())
A=[]
cnt=0
add=0
for i in range(4472):
    cnt +=i+1
    A.append((cnt,i+1))
for i in range(len(A)-1):
    if A[i][0]<=n<=A[i+1][0]:
        add=(A[i+1][1],A[i+1][0]-n)
        break
for i in range(add[0]):
    if i+1==add[1]:continue
    print(i+1)