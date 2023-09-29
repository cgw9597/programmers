def solution(my_str, n):
    from math import ceil
    answer=[]
    for i in range(ceil(len(my_str)/n)):
        answer.append(my_str[n*i:n+n*i])
    
    return answer