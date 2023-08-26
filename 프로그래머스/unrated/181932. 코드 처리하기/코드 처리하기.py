def solution(code):
    answer = ''
    mode = 0
    for idx,value in enumerate(code):
        if mode ==0 and value == '1':
            mode = 1
        elif mode == 1 and value == '1':
            mode = 0
        elif mode == 0 and value != '1' and idx%2 ==0:
            answer+=value
        elif mode ==1 and value !='1' and idx%2 !=0:
            answer+=value
    return answer if len(answer) !=0 else "EMPTY" 

# def solution(code):
#     answer = ''
#     mode=0
#     for i in range(len(code)):
#         if i%2==0 and mode==0:
#             answer+=code[i]
#         elif code[i]=="1" and mode==0:
#             mode=1
#         elif code[i]=="1" and mode==1:
#             mode=0
#         elif i%2!=0 and mode==1:
#             answer+=code[i]
#     return answer if answer!="" else "EMPTY"

