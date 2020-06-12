n=int(input())

print(0)
zero=input()
if zero=="Vacant":exit()

left,right=0,n
while left<right:
    mid=(left+right)//2
    print(mid)
    ans=input()
    if ans=="Vacant":exit()

    if (ans==zero and mid%2==1) or (ans!=zero and mid%2==0):right=mid+1
    else:left=mid