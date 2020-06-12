def words(n):
    if n==1:return "357"
    A=[]
    for i in "357":
        for j in words(n-1):
            A.append(i+j)
    return A


n=int(input())
m=len(str(n))

cnt=0
for j in range(3,m+1):
    for i in words(j):
        if n>=int(i) and ("3" in i and "5" in i and "7" in i):
            cnt +=1

print(cnt)