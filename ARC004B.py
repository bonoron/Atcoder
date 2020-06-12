n=int(input())
D=[int(input()) for _ in range(n)]
s=sum(D)
print(s)
print(max(0,2*max(D)-s))