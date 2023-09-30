def solution(n):
    result = []
    num = 2
    while n>=num:
        if n%num==0:
            result.append(num)
            n=n/num
        else:
            num+=1
    answer = list(set(result))
    return sorted(answer)