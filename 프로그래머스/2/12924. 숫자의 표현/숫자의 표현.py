def solution(n):
    answer = 0
    for i in range(1, n+1):
        plus = 0
        for j in range(i, n+1):
            plus += j
            if plus == n :
                answer+=1
                break
            elif plus > n:
                break
    return answer