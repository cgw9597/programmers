def solution(myStr):
    answer = []
    a = myStr.replace('b','a').replace('c','a').split('a')
    b = list(filter(None,a))
    return b if len(b)!=0 else ["EMPTY"]