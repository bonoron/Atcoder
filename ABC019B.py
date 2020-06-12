s=list(input())
n=len(s)
ans=""
word=s[0]
cnt=0
for i in range(len(s)):
    if word!=s[i]:
        ans +=word+str(cnt)
        word=s[i]
        cnt=1
    else:
        cnt +=1
ans +=word+str(cnt)
print(ans)