n,k=map(int,input().split())
if k==0:print(n**2);exit()
count=0
for i in range(k+1,n+1):
    p=n//i
    q=n%i
    count +=p*max(0,i-k)+max(0,q-k+1)
print(count)