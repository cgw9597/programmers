def solution(array, n):
    array.sort(reverse=True)
    answer = 0
    l = []
    a = {}
    l = list(map(lambda x: abs(n-x), array)) # 절대값 씌운 값들의 list 생성
    a = dict(zip(l, array)) # l과 array를 묶고 key:value의 형태로 만든다
    answer = a[min(a)]  # key가 가장 작은 값을 찾고 그 value 값을 출력한다.
    return answer

