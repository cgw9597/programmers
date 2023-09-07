import re
def solution(my_string):
    li = re.findall(r'[0-9]+',my_string)
    return sum(list(map(int,li)))