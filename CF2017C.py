s=input()
l,r=0,len(s)-1
cnt=0
while l<r:
    if s[r]!=s[l]:
        cnt +=1
        if s[l]=="x":l +=1
        elif s[r]=="x":r -=1
        else:print(-1);exit()
    else:
        r -=1
        l +=1
print(cnt)