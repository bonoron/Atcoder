s=input()
word={}
for i in s:
    if i not in word:word[i]=1
    else:word[i] +=1

A,B=0,0
for v,m in word.items():
    if m%2==1:
        m -=1
        A +=1
        B +=m//2
    else:
        B +=m//2

if A==0:print(B*2)
else:print(2*(B//A)+1)