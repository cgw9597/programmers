def solution(my_string, queries):
    my_string = list(my_string)
    for a,b in queries:
        my_string[a:b+1] = reversed(my_string[a:b+1])
    return ''.join(my_string)