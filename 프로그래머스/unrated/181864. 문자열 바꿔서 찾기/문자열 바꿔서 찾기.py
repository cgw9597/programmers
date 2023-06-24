def solution(myString, pat):
    answer = 0
    my_string = myString.replace('A','C').replace('B','A').replace('C','B')
    if pat in my_string:
        answer = 1
    return answer