dic={}
for i in range(int(input())):
    command,key=input().split()
    if command=="insert":
        dic[key]=True
    else:
        print("yes" if key in dic else "no")