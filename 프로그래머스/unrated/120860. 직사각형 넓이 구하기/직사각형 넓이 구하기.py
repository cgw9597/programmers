def solution(dots):
    wi = []
    hi = []
    for a,b in dots:
        wi.append(a)
        hi.append(b)
    return (max(wi)-min(wi)) * (max(hi)-min(hi))