n,k=map(int,input().split())
D=set(map(str,input().split()))

for i in range(n,10*n):
    num=set(list(str(i)))
    if i>=n and len(D&num)==0:
        print(i)
        exit()