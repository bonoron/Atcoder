x1,y1,x2,y2,t,v=map(int,input().split())
dis=t*v
n=int(input())
for x,y in [(map(int,input().split())) for i in range(n)]:
    if ((x-x1)**2+(y-y1)**2)**0.5+((x2-x)**2+(y2-y)**2)**0.5<=dis:
        print("YES")
        exit()
print("NO")