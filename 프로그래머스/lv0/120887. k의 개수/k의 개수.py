def solution(i, j, k):
    answer = []
    for num in range(i,j+1):
        answer.append(num)
    result = ''.join(map(str,answer))
    return result.count(str(k))