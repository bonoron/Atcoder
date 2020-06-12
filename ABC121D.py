def num(n):
    if n%2==0:
        if n%4==0:return n
        else:return n+1
    else:return (n+1)//2%2


a,b=map(int,input().split())
print(num(a-1)^num(b))