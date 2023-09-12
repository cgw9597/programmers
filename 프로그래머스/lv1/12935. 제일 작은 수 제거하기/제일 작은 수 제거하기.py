# def solution(arr):
#     arr.sort(reverse=True)
#     arr.pop()
#     if len(arr)==0:
#         arr = [-1]
#     return arr
def solution(arr):
    arr.remove(min(arr))
    
    return arr if len(arr)!=0 else [-1]