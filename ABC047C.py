s=input()
cnt=0
col=s[0]
for i in s:
    if i==col:continue
    else:
        col=i
        cnt +=1
print(cnt)