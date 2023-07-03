def solution(a, b):
    a_ = int(str(a)+str(b))
    b_ = int(str(b)+str(a))
    if a_>b_:
        answer = a_
    else:
        answer = b_
    return answer