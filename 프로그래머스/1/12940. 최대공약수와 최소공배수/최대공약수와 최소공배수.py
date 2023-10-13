def solution(n, m):
    import math
    gcd = math.gcd(n,m)
    lcm = (n*m) / gcd
    return [gcd, lcm]