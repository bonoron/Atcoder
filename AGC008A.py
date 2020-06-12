x,y=map(int,input().split())
ans=10**10
if x<y:ans=min(ans,y-x,abs(x+y)+1)
else:ans=min(ans,abs(x+y)+1,(x-y)+2)
print(ans)