def solution(str_list):
    for li in str_list:
        if li == 'l':
            return str_list[:str_list.index('l')]
        elif li == 'r':
            return str_list[str_list.index('r')+1:]
    return []