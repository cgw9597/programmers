def solution(numbers):
    li = ["zero", "one", "two", "three", "four", "five",
          "six", "seven", "eight", "nine"]
    for num, eng in enumerate(li):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)