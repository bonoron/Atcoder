s,t=list(input()),list(input())
length_s,length_t=len(s),len(t)

flag=0
for i in reversed(range(length_s-length_t+1)):
    word=s[i:i+length_t]
    cnt=0
    for j in range(length_t):
        if word[j]==t[j] or word[j]=="?":
            cnt +=1
        if cnt==length_t:
            flag=1
            s[i:i+length_t]=t
    if flag==1:break

s="".join(s).replace("?","a")
print(s if flag else "UNRESTORABLE")