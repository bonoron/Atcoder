def wage(B,id):
    sub_list=[i for i in range(n) if B[i]==id]
    if len(sub_list)==0:
        return 1
    else:
        sub=list(map(lambda x: wage(B,x),sub_list))
        return max(sub)+min(sub)+1


n=int(input())
B=[int(input())-1 for i in range(n-1)]
B.insert(0,-1)
print(wage(B,0))