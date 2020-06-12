s=list(input())
k=int(input())
count=0
re=""
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        if i==len(s)-1:
            re=s[-1]
        s[i]="A"
        count +=1

if s[0]==s[-1]:
    count +=1
    re=s[-1]
    s[-1]="A"

if (s[-1]=="A") and (s[-2]!=re):
    print((count*k)-1)
    exit()
print(count*k)