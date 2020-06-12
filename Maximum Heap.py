def maxHeapify(A,i):
    left,right=2*i,2*i+1
    if left<n and A[left]>A[i]:largest=left
    else:largest=i
    if right<n and A[right]>A[largest]:largest=right

    if largest!=i:
        A[i],A[largest]=A[largest],A[i]
        maxHeapify(A,largest)


def buildMaxHeap(A):
    for i in reversed(range(1,n//2+1)):
        maxHeapify(A,i)


n=int(input())+1
A=[0]+list(map(int,input().split()))
buildMaxHeap(A)
print(" ",end="")
print(*A[1:])