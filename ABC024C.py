n,d,k=map(int,input().split())
LR=[list(map(int,input().split())) for _ in range(d)]
ST=[list(map(int,input().split())) for _ in range(k)]

for s,t in ST:
    flag=1 if t>s else 0
    cnt=0
    for l,r in LR:
        cnt +=1
        if l<=s<=r:
            if flag:
                s=r
                if s>=t:
                    print(cnt)
                    break
            else:
                s=l
                if s<=t:
                    print(cnt)
                    break