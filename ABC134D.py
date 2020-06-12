n=int(input())
A=list(map(int,input().split()))
B,C=[0 for i in range(n+1)],[]
cnt=0
for i in range(1,n+1)[::-1]:
    sum_B=sum(B[j] for j in range(i,n+1,i))
    if sum_B%2!=A[i-1]:
        B[i]=1
        cnt +=1
        C.append(i)
print(cnt)
print(*[i for i in C[::-1]])