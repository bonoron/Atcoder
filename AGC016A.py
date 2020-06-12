def BFS(t):
    inf=10**3
    D=[inf for _ in range(n)]
    D[-1]=1

    for i in range(n):
        if s[i]==t:D[i]=0

    for i in range(1,n)[::-1]:
        if D[i-1]==inf:D[i-1]=D[i]+1

    return max(D)


s=input()
n=len(s)
ans=10**4
for i in range(26):
    ans=min(ans,BFS(chr(97+i)))
print(ans)