n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[]
S,ans=0,0
for a,b in zip(A,B):
    if a>=b:C.append(a-b)
    else:
        ans +=1
        S +=b-a
C.sort()
while S>0 and C:
    ans +=1
    S -=C.pop()
print(-1 if S>0 else ans)