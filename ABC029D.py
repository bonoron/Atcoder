n=input()
m=len(n)

DP=[[[0]*(m+1) for _ in range(2)] for _ in range(m+1)]
DP[0][0][0]=1

for i in range(1,m+1):
    for flag in range(2):
        num=9 if flag else int(n[i-1])
        for j in range(m):
            for k in range(num+1):
                if k==1:DP[i][flag or k<num][j+1] +=DP[i-1][flag][j]
                else:DP[i][flag or k<num][j] +=DP[i-1][flag][j]

ans=0
for i in DP[-1]:
    for j,k in enumerate(i):
        ans +=j*k
print(ans)

for i in range(m+1):
    print(DP[i])