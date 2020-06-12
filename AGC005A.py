from collections import deque
s=list(input())
A=deque([])
for i in s:
    if i=="S":A.append(i)
    elif i=="T":
        if len(A)==0 or A[-1]=="T":A.append(i)
        else:A.pop()
print(len(A))