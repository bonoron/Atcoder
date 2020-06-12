n=int(input())
NG=[int(input()) for i in range(3)]
cnt=0
if n in NG:print("NO");exit()
while n>0 and cnt!=100:
    if n-3 not in NG:n -=3
    else:
        if n-2 not in NG:n -=2
        elif n-1 not in NG:n -=1
        else:print("NO");exit()
    cnt +=1
print("YES" if n<=0 else "NO")