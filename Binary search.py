n=int(input())
s=list(map(int,input().split()))
q=int(input())
t=list(map(int,input().split()))

def BinarySearch(s,n,point):
    left,right=0,n
    while left<right:
        mid=(left+right)//2
        if s[mid]==point:
            return 1
        elif point<s[mid]:
            right=mid
        elif point>s[mid]:
            left=mid+1
    return 0

count=0
for i in t:
    if BinarySearch(s,n,i):count +=1
print(count)