def solution(n):
    import math
    answer = []
    for i in range(2000):
        if math.factorial(i)<=n:
            answer.append(i)
    
    return max(answer)