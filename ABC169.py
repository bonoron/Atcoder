n=int(input())
AB=[list(map(int,input().split())) for _ in range(n)]

Count=set()
for a,b in AB:
    Count.add(a)
    Count.add(b)
Count=sorted(Count)
