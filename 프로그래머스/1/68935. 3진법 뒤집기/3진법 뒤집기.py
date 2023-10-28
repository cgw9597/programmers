def solution(n):
    answer = 0
    li = []
    if n<3:
        return n
    while True:
        a = n%3
        li.append(a)
        n = n//3
        if n in(1,2):
            li.append(n)
            break
    li.reverse()
    for i in range(len(li)):
        answer += li[i] * 3**i
    return answer