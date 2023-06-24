def solution(myString, pat):
    answer = 0
    if pat.upper() in myString.upper():
        answer = 1
    return answer

# def solution(myString, pat):
#     return int(pat.lower() in myString.lower())