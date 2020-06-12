from collections import Counter

n=int(input())
V=list(map(int,input().split()))
V_1=[(0,0)]+sorted(Counter([V[i] for i in range(n) if i%2==0]).items(), key=lambda x:x[1])
V_2=[(0,0)]+sorted(Counter([V[j] for j in range(n) if j%2==1]).items(), key=lambda x:x[1])

a,b=V_1[-1][0],V_2[-1][0]

if a==b:
    if V_1[-2][1]>V_2[-2][1]:a=V_1[-2][0]
    else:b=V_2[-2][0]

cnt=0
for i in range(n):
    if i%2==0:
        if V[i]!=a:cnt +=1
    else:
        if V[i]!=b:cnt +=1

print(cnt)