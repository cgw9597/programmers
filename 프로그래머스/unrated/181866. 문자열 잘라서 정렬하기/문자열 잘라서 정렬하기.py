def solution(myString):
    answer = []
    my_string = ''.join(myString).split('x')
    for i in my_string:
        if i != "":
            answer.append(i)
    answer.sort()
    return answer