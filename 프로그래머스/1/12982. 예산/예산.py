def solution(d, budget):
    cnt = 0
    d = sorted(d)
    for i in d:
        budget -= i
        if budget < 0:
            break
        cnt += 1
    return cnt