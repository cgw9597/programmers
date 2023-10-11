def solution(arr):
    answer = []
    if len(arr) > len(arr[0]):
        for i in arr:
            answer.append(i+[0]*(len(arr)-len(arr[0])))
    elif len(arr) < len(arr[0]):
        for _ in range(len(arr[0])-len(arr)):
            arr.append([0]*len(arr[0]))
        answer = arr
    else:
        answer = arr
    return answer