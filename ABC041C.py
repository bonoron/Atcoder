n=int(input())
A=list(map(int,input().split()))
A=sorted([(A[i],i+1) for i in range(n)])
for i in A[::-1]:print(i[1])