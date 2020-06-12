mod=10**9+7
n=int(input())
A=list(input())+["#"]
B=list(input())+["*"]
C=""

i=0
while i<n:
    if A[i]==B[i]:
        C +="X";i +=1
    elif A[i]==A[i+1] and B[i]==B[i+1]:
        C +="Y";i +=2

cnt=3 if C[0]=="X" else 6
for i in range(1,len(C)):
    word=C[i-1]+C[i]
    if word=="XY":cnt *=2
    elif word=="XX":cnt *=2
    elif word=="YX":cnt *=1
    elif word=="YY":cnt *=3
    cnt %=mod

print(cnt)