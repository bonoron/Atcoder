import sys
sys.setrecursionlimit(10**6)


def DFS(num):
    A.add(int(num))
    n=int(num[-1])
    for i in (max(n-1,0),n,min(n+1,9)):
        i=str(i)
        A.add(int(num+i))
        if len(num)<=8:DFS(num+i)


n=int(input())
A=set()
for i in range(1,10):
    DFS(str(i))
A=sorted(A)
print(A[n-1])