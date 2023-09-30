def solution(numbers, k):
    idx = 0
    for _ in range(k-1):
        idx = (idx + 2) % len(numbers)
    return numbers[idx]

# def solution(numbers, k):
#     return numbers[2 * (k - 1) % len(numbers)]