N=int(input())
num=[0]+list(map(int,input().split()))
for i in range(N):
    num[i+1]=num[i]+num[i+1]
num=sorted(num)+[-1]
count,n=0,0
flag=num[0]
for i in num:
    if i==flag:
        n +=1
    else:
        count +=(n*(n-1))//2
        flag=i
        n=1
print(count)