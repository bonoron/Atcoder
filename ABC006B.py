def tori(n):
    mod=10007
    DP=[0]*10**6
    DP[2]=1
    for i in range(3,n):
        DP[i]=(DP[i-1]+DP[i-2]+DP[i-3])%mod
    return DP[n-1]


print(tori(int(input())))