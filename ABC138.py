import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

n,q=map(int,input().split())
A=[[] for i in range(n)]
node=[0]*n

for i in range(n-1):
    a,b=map(int,input().split())
    a -=1;b -=1
    A[a].append(b)
    A[b].append(a)

for i in range(q):
    p,x=map(int,input().split())
    node[p-1] +=x


def calculate(num,pre=-1):
    for i in A[num]:
        if i==pre:continue
        node[i] +=node[num]
        calculate(i,num)


calculate(0)
print(*node)