def solution(num_list):
    answer = 0
    a= 0
    b = 0
    for i in num_list[0::2]:
        a += i
    for j in num_list[1::2]:
        b += j
    if a>b:
        answer = a
    elif a<b:
        answer = b
    else:
        answer = a
    return answer

#def solution(num_list):
#    return max(sum(num_list[::2]), sum(num_list[1::2]))