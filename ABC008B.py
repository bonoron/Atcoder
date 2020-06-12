n=int(input())
dic={}
for i in range(n):
    s=input()
    if s not in dic:dic[s]=1
    else:dic[s] +=1
print(sorted(dic.items(), key=lambda x: -x[1])[0][0])