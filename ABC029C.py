def k(n):
    if n==1:return "abc"
    x=[]
    for i in "abc":
        for j in k(n-1):
            x.append(i+j)
    return x
print(*k(int(input())),sep="\n")