t=int(input())
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))+[float("inf")]

a,b=0,0
while a<n and b<m:
    if A[a]<=B[b]<=A[a]+t:
        a +=1;b +=1
    else:
        a +=1

print("yes" if B[b]==float("inf") else "no")