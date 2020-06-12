s=input()
t=input()
words="atcoder"
for i,j in zip(s,t):
    if i==j:continue
    elif i=="@" and j in words:continue
    elif j=="@" and i in words:continue
    else:print("You will lose");exit()
print("You can win")