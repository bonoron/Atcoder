n,l=map(int,input().split())
A=list(map(int,input().split()))
add=0
for i in range(1,n):
    if A[i]+A[i-1]>=l:
        add=i+1
        break
if add==0:print("Impossible");exit()
print("Possible")
for i in range(1,add-1):print(i)
for i in [j for j in range(add,n)][::-1]:print(i)
print(add-1)