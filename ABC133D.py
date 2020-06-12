n=int(input())
A=list(map(int,input().split()))
ans=[sum(A)-2*(sum(A[1::2]))]
for i in range(n-1):
    ans.append(2*A[i]-ans[i])
print(*ans)