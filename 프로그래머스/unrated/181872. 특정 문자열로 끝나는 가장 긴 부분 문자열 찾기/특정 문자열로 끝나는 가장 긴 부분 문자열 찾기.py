def solution(myString, pat):
    answer = ''
    a = 0
    for idx,value in enumerate(myString):
        if value == pat[-1]:
            a = idx
    return myString[0:a+1]