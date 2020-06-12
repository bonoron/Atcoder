n=int(input())
S=[input() for i in range(n)]
a,b,c=0,0,0
cnt=0
for i in S:
    if i[0]=="B" and i[-1]=="A":c +=1
    elif i[0]=="B":a +=1
    elif i[-1]=="A":b +=1
    for j in range(len(i)-1):
        if i[j]+i[j+1]=="AB":cnt +=1

if c==0:cnt +=min(a,b)
elif a+b==0:cnt +=c-1
elif c!=0 and a+b>0:cnt +=min(a,b)+c
print(cnt)