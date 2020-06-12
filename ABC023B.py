n=int(input())
s=input()
word="b"
ans=["b"]
for i in range(100):
    for j in range(3):
        if j==0:word="a"+word+"c"
        elif j==1:word="c"+word+"a"
        elif j==2:word="b"+word+"b"
        ans.append(word)

for i,j in enumerate(ans):
    if j==s:
        print(i)
        exit()
    elif len(j)>n:
        print(-1)
        exit()