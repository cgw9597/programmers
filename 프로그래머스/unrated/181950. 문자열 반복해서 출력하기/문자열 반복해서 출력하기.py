a, b = input().strip().split(' ')
b = int(b)
a = str(a)
if len(a) >=1 and len(a) <=10 and b>=1 and b<=5:
    print(a*b)