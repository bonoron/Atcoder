n=input()
s=list(map(int,input().split()))
q=input()
t=list(map(int,input().split()))
count=0
for i in t:
    if i in s:count +=1
print(count)

#番兵を使った解き方
"""n=input()
s=list(map(int,input().split()))
q=input()
t=list(map(int,input().split()))
count=0
for i in t:
    j=0
    s.append(i)
    while s[j]!=i:j +=1
    s.pop()
    if j==int(n):continue
    else:count +=1
print(count)"""