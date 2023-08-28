def solution(arr, queries):
    answer = []
    x=[]
    for a, b in queries:
        x = arr[a]
        arr[a] = arr[b]
        arr[b] = x
    return arr