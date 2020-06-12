s=input()[::-1]
words=["dreamer","eraser","dream","erase"]
add=0
while add!=len(s):
    cnt=0
    for i in words:
        length=len(i)
        word=s[add:add+length][::-1]
        if word==i:
            add +=length
            break
        else:cnt +=1
    if cnt==4:print("NO");exit()
print("YES")