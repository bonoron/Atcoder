from bisect import bisect_left,bisect_right
n=int(input())
A=sorted(list(map(int,input().split())))
B=list(map(int,input().split()))
C=sorted(list(map(int,input().split())))

ans=0
for b in B:
    index_a=bisect_left(A,b)
    index_c=bisect_right(C,b)
    ans +=index_a*(n-index_c)

print(ans)