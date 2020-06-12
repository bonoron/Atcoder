from collections import deque
n=int(input())
num,mod=(n//5)%6,n%5
N=["1","2","3","4","5","6"]
N=deque(N)
for i in range(num):
    N.append(N.popleft())
for i in range(mod):
    N[i%5],N[i%5+1]=N[i%5+1],N[i%5]
print("".join(N))
print()