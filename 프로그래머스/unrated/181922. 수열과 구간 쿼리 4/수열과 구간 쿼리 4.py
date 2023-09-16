def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        for i in range(len(arr[s:e+1])):
            if i>=s and i%k ==0:
                arr[i]+=1
    return arr