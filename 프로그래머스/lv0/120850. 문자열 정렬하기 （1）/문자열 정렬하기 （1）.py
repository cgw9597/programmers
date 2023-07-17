def solution(my_string):
    answer = []
    string_list = list(my_string)
    for i in range(len(string_list)):
        if string_list[i].isdigit():
            answer.append(int(string_list[i]))
    answer.sort()
    return answer
