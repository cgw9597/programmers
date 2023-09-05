# def solution(i, j, k):
#     answer = []
#     for num in range(i,j+1):
#         answer.append(num)
#     result = ''.join(map(str,answer))
#     return result.count(str(k))

def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
    return answer