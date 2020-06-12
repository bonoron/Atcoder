n=input()
m=len(n)-1

ans=0
for i in range(2**m):
    num=format(i,"b").zfill(m)
    N=list(n)
    for j,k in enumerate(num):
        if k=="1":N[j]=N[j]+"+"
    ans +=eval("".join(N))
print(ans)