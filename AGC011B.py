n=int(input())
A=sorted(list(map(int,input().split())))
sum_A=sum(A)
cnt=1
for i in reversed(range(n)):
    sum_A -=A[i]
    if sum_A*2>=A[i]:
        cnt +=1
    else:break
print(cnt)