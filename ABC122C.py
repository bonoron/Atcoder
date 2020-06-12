n,q=map(int,input().split())
s=input()+"P"
A=[list(map(int,input().split())) for i in range(q)]
B=[0]*(n+1)
cnt=0
for i in range(1,n):
    if s[i-1]+s[i]=="AC":cnt +=1
    B[i+1]=cnt

for l,r in A:print(B[r]-B[l])