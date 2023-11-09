N = int(input())
T = []
P = []
d = [0]*N

for i in range(N):
    a, b = list(map(int, input().split()))
    T.append(a)
    P.append(b)
for j in range(N):
    if T[j] + j <= N:  # 퇴사전 상담
        d[j] = P[j]  # 그 금액 저장
        for k in range(j):
            if k + T[k] <= j:  # 이전 상담이 오늘 전에 가능하면
                d[j] = max(d[j], d[k]+P[j])  # 이전금액+당일금액 의 최대값 저장 
print(max(d))