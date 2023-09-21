a = int(input())
li=[]
for _ in range(a):
    H, W, N = list(map(int,input().split()))
    if N%H ==0:
        li.append(H*100+N//H)
    else:
        li.append((N%H)*100+N//H+1)
for i in li:
    print(i)