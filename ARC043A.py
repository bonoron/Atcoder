n,a,b=map(int,input().split())
try:
    S=[int(input()) for i in range(n)]
    p=b/(max(S)-min(S))
    S=[S[i]*p for i in range(n)]
    q=a-sum(S)/n
    print(p,q)
except:print(-1)