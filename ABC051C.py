sx,sy,tx,ty=map(int,input().split())
ans=""
width=tx-sx
length=ty-sy
A,B,C,D="U"*length,"R"*width,"D"*length,"L"*width
for i in range(2):
    if i==0:ans +=A+B+C+D
    else:ans +="L"+A+"UR"+B+"DR"+C+"DL"+D+"U"
print(ans)