n=int(input())
s=input()

L,R=0,0
l,r=0,0
for i in s:
    if i=="(":
        l +=1
    else:
        l -=1
        L=min(L,l)

for i in s[::-1]:
    if i==")":
        r +=1
    else:
        r -=1
        R=min(R,r)

print("("*-L+s+")"*-R)