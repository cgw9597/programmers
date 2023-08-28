def solution(my_string, m, c):
    return my_string[c-1::m]




# def solution(my_string, m, c):
#     answer = []
#     li = []
#     for i in range(len(my_string)//m):
#         li.append(my_string[i*m:(i+1)*m])
#     for j in range(len(li)):
#         answer.append(li[j][c-1])
#     return ''.join(answer)