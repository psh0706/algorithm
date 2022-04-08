arr = list(map(int, list(input())))
arr.sort(key=lambda x: -x)
print("".join(map(str, arr)))

"""
가볍게 풀어본 정렬문제
"""