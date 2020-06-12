n,m=map(int,input().split())
name=input()
kit=input()

cnt=1
stock={}
for i in kit:
    if i not in stock:stock[i]=1
    else:stock[i] +=1

for i in name:
    if i not in stock:
        print(-1);exit()
    elif stock[i]>0:
        stock[i] -=1
    else:
        stock[i] -=1
        for j in kit:
            stock[j] +=1
        cnt +=1

print(cnt)