def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            answer+=(arr[i:])
            break
    if answer == []:
        return [-1]
    while answer[-1]!=2:
        answer.pop()
    return answer