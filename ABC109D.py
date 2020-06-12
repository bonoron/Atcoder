h,w=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(h)]

C=[]
for i in range(h):
    flag=1 if i%2==0 else -1
    for j in range(w)[::flag]:
        if A[i][j]%2==1:
            if 0<=j+flag<w:
                C.append([i,j,i,j+flag])
                A[i][j+flag] +=1
            elif 0<=i+1<h:
                C.append([i,j,i+1,j])
                A[i+1][j] +=1

print(len(C))
for i in C:
    print(*list(map(lambda x:x+1,i)))