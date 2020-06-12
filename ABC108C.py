n,k=map(int,input().split())
count,point=0,0
if k%2!=0:
    while k*(count+1)<=n:
        count +=1
    print(count**3)
else:
    for i in range(1,n+1):
        if i%k==0:point +=1
        elif i*2%k==0:count +=1
    print(count**3+point**3)