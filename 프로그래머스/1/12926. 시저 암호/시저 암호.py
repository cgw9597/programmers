def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer+=i
        elif i.isupper():
            num = (ord(i)+n-ord('A'))%26+ord('A')
            answer+=chr(num)
        elif i.islower():
            num = (ord(i)+n-ord('a'))%26+ord('a')
            answer+=chr(num)
    return answer