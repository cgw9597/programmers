def solution(my_string):
    import re
    li = re.findall(r'[0-9]+',my_string)
    answer = sum(list(map(int,li)))
    return answer