H,W,A,B = map(int,input().split())

for i in range(H):
    if i < B:
        print("0"*A + "1"*(W-A))
    else:
        print("1"*A + "0"*(W-A))