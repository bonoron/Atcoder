n,m=map(int,input().split())
H,M=(360/12)*(n%12)+(30/60)*m,(360/60)*m
print(min(abs(H-M),abs(360-abs(H-M))))