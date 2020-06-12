n,k=map(int,input().split())
box=[0]+list(map(int,input().split()))
for i in range(n):box[i+1]=box[i]+box[i+1]
count,add,point=0,0,0
for i in range(n):
    try:
        while box[add]-box[i]<k:
            add +=1
            point +=1
        count +=n-point+1
    except:break
print(count)