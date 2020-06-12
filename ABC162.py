n=int(input())
s=input()

ans=s.count("R")*s.count("B")*s.count("G")
for i in range(n):
    for j in range(i+1,n):
        k=2*j-i
        if k>=n:break
        if s[i]!=s[j] and s[j]!=s[k] and s[i]!=s[k]:
            ans -=1

print(ans)