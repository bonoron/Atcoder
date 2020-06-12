def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x
def lcm(x,y):
    return (x*y)//gcd(x,y)
n=int(input())
t=int(input())
for i in range(n-1):
    t=lcm(t,int(input()))
print(t)