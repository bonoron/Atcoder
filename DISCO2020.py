h,w,k=map(int,input().split())
MAP=[list(input()) for i in range(h)]
ans=[[0 for i in range(w)] for j in range(h)]
cnt=0
line=[]

for i in range(h):
    if "#" not in MAP[i]:
        line.append(i)
        continue
    start=cnt
    for j in range(w):
        if MAP[i][j]=="#" and cnt!=k:
            cnt +=1
            ans[i][j]=cnt
        else:
            if cnt==start:ans[i][j]=start+1
            else:ans[i][j]=cnt

ans.insert(0,["*"]*w)
ans.append(["*"]*w)
while len(line)!=0:
    for i in line:
        i=i+1
        if ans[i+1][0]!=0 and ans[i+1][0]!="*":
            ans[i]=ans[i+1]
            line.remove(i-1)
        elif ans[i-1][0]!=0 and ans[i-1][0]!="*":
            ans[i]=ans[i-1]
            line.remove(i-1)

for i in range(1,h+1):
    print(*ans[i])