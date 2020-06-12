from collections import deque
n,d,a=map(int,input().split())
XH=sorted([list(map(int,input().split())) for i in range(n)])+[float("inf"),float("inf")]

for i in range(n):
    x,h=XH[i]
    wid=