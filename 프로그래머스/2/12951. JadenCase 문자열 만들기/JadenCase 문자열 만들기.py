def solution(s):
    answer = ''
    li = list(s.lower())
    for i in range(len(li)):
        if li[i].isalpha() and len(answer)  == 0:
            answer+=li[i].upper()
        elif li[i].isdigit():
            answer+=li[i]
        elif li[i-1].isdigit():
            answer+=li[i]
        elif li[i-1].isalpha():
            answer+=li[i]
        elif li[i]==" ":
            answer+=li[i]
        elif li[i-1]==" ":
            answer+=li[i].upper()
    return answer