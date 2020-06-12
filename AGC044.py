t=int(input())
A,B=[],[2,3,5]
for i in range(t):
    n,a,b,c,d=map(int,input().split())
    for j,k in enumerate([a,b,c]):
        coin,num=d,1
        while num<max(0,n-10**5):
            coin +=k
            num *=B[j]
        print(coin,num)
    print()