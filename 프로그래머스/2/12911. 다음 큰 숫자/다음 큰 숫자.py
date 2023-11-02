def solution(n):
    m = n+1
    N = format(n,'b').count('1')
    while True:
        M = format(m,'b').count('1')
        if N == M:
            answer = m
            break
        else:
            m+=1
    return answer