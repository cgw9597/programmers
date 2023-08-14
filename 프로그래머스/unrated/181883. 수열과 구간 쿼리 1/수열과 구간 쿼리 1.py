# def solution(arr, queries):
#     answer = []
#     for i in queries:
#         answer = [ j + 1 for j in arr[i[0]:i[1]+1]]
#         arr[i[0]:i[1]+1] = answer
#     return arr

def solution(arr, queries):
    for l,r in queries:
        for i in range(l,r+1):
            arr[i]+=1
    return arr
