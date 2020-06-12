n,m=map(int,input().split())
FF=[list(map(int,input().split())) for i in range(m)]

nums=[[] for i in range(n+1)]
for a,b in FF:
    nums[a] +=[b]
    nums[b] +=[a]

for i in range(1,n+1):
    target=nums[i]+[i]
    ans=[]
    for j in nums[i]:
        ans +=nums[j]
    print(len(set(ans)-set(target)))