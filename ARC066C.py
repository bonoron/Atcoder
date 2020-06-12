from collections import Counter
mod=10**9+7
n=int(input())
A=list(map(int,input().split()))
Count=sorted(Counter(A).items())
cnt=0
if n%2==1:
    if Count.pop(0)[1]==1:
        point=2
        for v,m in Count:
            if v==point and m==2:
                cnt +=1
                point +=2
        print((2**cnt)%mod)
    else:print(0);exit()
else:
    point=1
    for v,m in Count:
        if v==point and m==2:
            cnt +=1
            point +=2
        else:print(0);exit()
    print((2**cnt)%mod)