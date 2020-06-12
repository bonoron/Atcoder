def digitDP(n):
    n=str(n)
    m=len(n)
    DP=[[[0]*2 for _ in range(2)] for _ in range(m+1)]
    DP[0][0][0]=1

    for i in range(1,m+1):
        for flag in range(2):
            num=9 if flag else int(n[i-1])
            for j in range(2):
                for k in range(num+1):
                    if (k==4 or k==9) and j==0:
                        DP[i][flag or k<num][j+1] +=DP[i-1][flag][j]
                    else:
                        DP[i][flag or k<num][j] +=DP[i-1][flag][j]

    ans=DP[-1][0][1]+DP[-1][1][1]

    return ans


a,b=map(int,input().split())
A=digitDP(a-1)
B=digitDP(b)

print(B-A)