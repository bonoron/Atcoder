h,w,d=map(int,input().split())
box=list(list(map(int,input().split())) for i in range(h))
q=int(input())
order=[list(map(int,input().split())) for i in range(q)]

S=[0]*(h*w+1)
add={}

for i in range(h):
    for j in range(w):
        add[box[i][j]]=[i,j]

for k in range(d+1,h*w+1):
    x,y=add[k]
    i,j=add[k-d]
    S[k]=S[k-d]+abs(x-i)+abs(y-j)

for s,g in order:
    print(S[g]-S[s])

"""h,w,d=map(int,input().split())
box=[list(map(int,input().split())) for i in range(h)]
adress={}
for i in range(h):
    for j in range(w):
        adress[box[i][j]]=[i,j]

q=int(input())
order=[list(map(int,input().split())) for i in range(q)]

#1～h*wなので0がはいってきてしまっているから+1
#先に全部の記録を行った方が早いのか計算量の見積もりが大事

S=[0]*(h*w+1)
for k in range(d+1,h*w+1):
    x,y=adress[k]
    i,j=adress[k-d]
    S[k]=S[k-d]+abs(x-i)+abs(y-j)

for x,y in order:
    print(S[y]-S[x])"""