def solution(myString, pat):
    answer = 0
    my_string = myString.upper()
    pa_t = pat.upper()
    if pa_t in my_string:
        answer = 1
    return answer