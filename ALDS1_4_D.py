n,k=map(int,input().split())
A=[int(input()) for i in range(n)]

def track_num(n):
    cnt,track=0,1
    for i in A:
        if cnt+i>n:
            track +=1
            cnt=i
        else:
            cnt +=i
    return track

def Binaryserch():
    left,right=max(A),10**10
    ans=0
    while left<right:
        mid=(left+right)//2
        track=track_num(mid)
        if track<=k:
            ans=mid
            right=mid
        elif track>k:
            left=mid+1
    return ans

print(Binaryserch())