n=int(input())
x,y=0,0
for i in sorted([int(input()) for i in range(n)])[::-1]:
    if x>=y:y +=i
    else:x +=i
print(max(x,y))