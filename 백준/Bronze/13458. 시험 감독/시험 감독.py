N = int(input())  # 시험장 개수
A = list(map(int, input().split()))  # 응시자수
B, C = list(map(int, input().split()))  # 총, 부
cnt = N

for i in A:
    i-=B
    if i>0:
        if i%C:
            cnt += i//C + 1
        else:
            cnt += i//C
print(cnt)