def solution(myString):
    my_string = ' '.join(myString.split('x')).split()
    answer = sorted(my_string)
    return answer

# def solution(myString):
#     answer = ' '.join(myString.split('x')).split()
#     return sorted(answer)