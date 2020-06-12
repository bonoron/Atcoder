s=input()
m=len(s)

ans=0
for i in range(m-3):
    for j in range(i+4,m+1):
        num=int(s[i:j])
print(ans)