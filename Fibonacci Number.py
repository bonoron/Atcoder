def make_fibonacci(n):
    F[0]=F[1]=1
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]


F=[0]*45
n=int(input())
make_fibonacci(n)
print(F[n])