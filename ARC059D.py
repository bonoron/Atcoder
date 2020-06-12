s=input()
n=len(s)
A,B=-1,-1
for i in range(n-1):
    if s[i]==s[i+1]:
        A,B=i+1,i+2

for i in range(n-2):
    if s[i]==s[i+2]:
        A,B=i+1,i+3

print(A,B)