n,k=map(int,input().split())
S=input()+"*"

A=[0] if S[0]=="1" else []
cnt,fig=0,S[0]
for i in range(n+1):
    if fig!=S[i]:
        A.append(cnt)
        fig=S[i]
        cnt=1
    else:cnt +=1

if S[-2]=="0":A.append(0)
num=2*(k+1)
B=[[0,0]] if S[0]=="0" else []
for i in range(1,len(A)):
    A[i]=A[i]+A[i-1]
for i in range(0,len(A),2):
    B.append([A[i],A[i+1]])

C=[]
left=0
for i in range(max(0,len(B)-k)):
    C.append(B[k+i][1]-B[left+i][0])
print(max(C) if len(B)-k>0 else B[-1][1])