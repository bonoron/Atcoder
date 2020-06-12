n,x=map(int,input().split())
A=list(map(int,input().split()))
bin_str=format(x,"b").zfill(n)
cnt=0
for i,j in enumerate(bin_str[::-1]):
    cnt +=A[i]*int(j)
print(cnt)