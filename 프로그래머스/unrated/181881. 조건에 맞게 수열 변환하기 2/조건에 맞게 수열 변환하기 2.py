def solution(arr):
    answer = 0
    while True:
        arr2=[]
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i]%2==0:
                arr2.append(arr[i]/2)
            elif arr[i] < 50 and arr[i]%2!=0:
                arr2.append(arr[i]*2+1)
            else:
                arr2.append(arr[i])
        if arr2 == arr:
            break
        arr = arr2
        answer+=1
    return answer