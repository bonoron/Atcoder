def combination(n,r,mod=10**9+7):
    r=min(r,n-r)
    up,down=1,1
    for i in range(r):
        up=up*(n-i)%mod
        down=down*(i+1)%mod
    return up*pow(down,mod-2,mod)%mod


x,y=map(int,input().split())
n,m=(2*y-x)//3,(2*x-y)//3
if (x+y)%3!=0 or n<0 or m<0:print(0);exit()
print(combination(n+m,m))