def solution(n):
    F = [0,1] + [0]*(n-1)
    for i in range(1,n):
        F[i+1] = F[i] + F[i-1]
    return F[n]%1234567