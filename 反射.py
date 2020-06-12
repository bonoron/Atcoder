def project(x,y):
    base=[x2-x1,y2-y1]
    hypo=[x-x1,y-y1]
    r=(base[0]*hypo[0]+base[1]*hypo[1])/(base[0]**2+base[1]**2)
    return x1+base[0]*r,y1+base[1]*r


def reflect(x,y):
    px,py=project(x,y)
    return x+(px-x)*2,y+(py-y)*2


x1,y1,x2,y2=map(int,input().split())
q=int(input())
for i in range(q):
    x,y=map(int,input().split())
    print(*reflect(x,y))