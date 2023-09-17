def solution(arr):
    count = 0
    arr_len = len(arr)
    while arr_len > 1:
        arr_len = arr_len / 2
        count+=1    
    return arr + [0]*(2**count - len(arr))