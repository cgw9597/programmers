def solution(a, b):
    a_ = int(str(a)+str(b))
    b_ = int(str(b)+str(a))
    answer = max(a_,b_)
    return answer