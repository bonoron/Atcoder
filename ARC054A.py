l,x,y,s,d=map(int,input().split())
speed_r=x+y
speed_l=max(0.001,y-x)
print(min((d-s)/speed_r,(l-d+s)/speed_l) if d>s else min((l-s+d)/speed_r,(s-d)/speed_l))
print()