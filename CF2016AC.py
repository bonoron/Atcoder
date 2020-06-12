s=input()
k=int(input())
m=len(s)
box=[chr(i) for i in range(97,97+26)]

word={j:26-i for i,j in enumerate(box)}
word_num={26-i:j for i,j in enumerate(box)}
number={i:j for i,j in enumerate(box)}
ans=""

for i,j in enumerate(s):
    if i==m-1:
        k %=26
        if k>=word[j]:ans +=number[k-word[j]]
        else:ans +=word_num[word[j]-k]
    elif word[j]<=k:
        k -=word[j]
        ans +="a"
    else:ans +=j

print(ans)