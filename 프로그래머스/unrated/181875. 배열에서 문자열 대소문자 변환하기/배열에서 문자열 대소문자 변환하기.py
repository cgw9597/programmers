def solution(strArr):
    answer = []
    for i, _ in enumerate(strArr):
        if i%2 != 0:
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
    return answer