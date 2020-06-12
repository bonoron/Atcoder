s=input().replace("BC","D")+"E"

A=[]
word=""
for i in s:
    if i=="A" or i=="D":word +=i
    else:A.append(word);word=""

cnt=0
for i in A:
    a=0
    for j in i:
        if j=="A":a +=1
        else:cnt +=a

print(cnt)