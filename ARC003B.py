n=int(input())
S=sorted([list(reversed(input())) for i in range(n)])
for i in range(n):print("".join(S[i])[::-1])