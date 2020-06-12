A,B,K,L=map(int,input().split())
if B/L>=A:print(A*K);exit()
else:print(B*(K//L)+A*(K%L) if A*(K%L)<=B else B*(K//L)+B)