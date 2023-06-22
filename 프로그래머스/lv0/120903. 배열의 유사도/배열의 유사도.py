def solution(s1, s2):
    same = list(set(s1)&set(s2))
    answer = len(same)
    return answer