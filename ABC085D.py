n,h=map(int,input().split())
A=list(tuple(map(int,input().split())) for i in range(n))
A,B=zip(*A)
a=max(A)
count=0
for i in sorted(B)[::-1]:
    if h<=0:break
    elif i>=a:
        count +=1
        h -=i
if h>0:
    if h%a==0:count +=h//a
    else:count +=h//a+1

print(count)