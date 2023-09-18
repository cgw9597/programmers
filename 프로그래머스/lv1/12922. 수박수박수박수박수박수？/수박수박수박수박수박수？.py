def solution(n):
    result =  ""
    for i in range(n):
        li = ["수","박"] * n
        result += li[i]
    
    return result