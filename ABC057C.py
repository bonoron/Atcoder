ans=100
n=int(input())
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        a,b=str(i),str(n//i)
        ans=min(ans,max(len(a),len(b)))
print(ans)