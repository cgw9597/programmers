def solution(t, p):
    T = len(t)
    P = len(p)
    li = []
    for i in range(T-P+1):
        li.append(t[i:i+P])
    n_li = list(map(int,li))
    result = 0
    for j in n_li:
        if j <= int(p):
            result+=1
    return result