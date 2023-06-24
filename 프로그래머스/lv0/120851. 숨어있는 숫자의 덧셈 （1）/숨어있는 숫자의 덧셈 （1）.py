# import re
# def solution(my_string):
#     answer = 0
#     my_str = re.findall('\d',my_string)
#     a = map(int,my_str)
#     answer = sum(a)
#     return answer

def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer += int(i)
        except:
            pass

    return answer
