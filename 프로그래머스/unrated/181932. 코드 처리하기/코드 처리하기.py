def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'

# def solution(code):
#     answer = ''
#     mode = 0
#     for idx,value in enumerate(code):
#         if mode ==0 and value == '1':
#             mode = 1
#         elif mode == 1 and value == '1':
#             mode = 0
#         elif mode == 0 and value != '1' and idx%2 ==0:
#             answer+=value
#         elif mode ==1 and value !='1' and idx%2 !=0:
#             answer+=value
#     return answer if len(answer) !=0 else "EMPTY"


