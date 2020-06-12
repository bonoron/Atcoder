n=int(input())
M=[list(input()) for i in range(n)]
T=[]
for i in range(9):
    axis=[]
    for j in range(n):
        axis.append(M[j][i])
    T.append(axis)

cnt=0
for i in T:
    i=["."]+i
    for j in range(len(i)):
        if i[j]==".":continue
        else:
            if i[j]=="o" and i[j-1]!="o":cnt +=1
            elif i[j]=="x":cnt +=1

print(cnt)