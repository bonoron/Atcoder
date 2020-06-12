n=int(input())
A=list(map(int,input().split()))

if sum(A)%n!=0:print(-1);exit()

pe=sum(A)//n
if pe==0:print(0);exit()

cnt,island,man=0,1,0
for i in range(n):
    man +=A[i]
    if man//island==pe and man%island==0:
        cnt +=island-1
        island,man=1,0
    else:
        island +=1
print(cnt)