from itertools import permutations
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
for p,q,r in permutations(B,3):
    ans=max(ans,(A[0]//p)*(A[1]//q)*(A[2]//r))
print(ans)