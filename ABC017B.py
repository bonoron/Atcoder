n=input()
words=["ch","o","k","u"]
point,s=0,""
while 1:
    flag=0
    for i in words:
        if n[point:len(i)+point]==i:
            point +=len(i)
            s +=i
            flag=1
            break
    if flag==0:break

print("YES" if s==n else "NO")