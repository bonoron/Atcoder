import math
n=int(input())
line=[list(map(int,input().split())) for i in range(n)]
cnt=0
for a,b in line[::-1]:
    A=a+cnt
    if A%b==0:continue
    elif A<=b:cnt +=b-A
    else:cnt +=b*(math.ceil(A/b))-A
print(cnt)