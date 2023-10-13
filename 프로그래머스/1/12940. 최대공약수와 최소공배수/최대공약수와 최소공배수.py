def solution(n, m):
    import math
    gcd = math.gcd(n,m)
    lcm = gcd * (n/gcd) * (m/gcd)
    return [gcd, lcm]