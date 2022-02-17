n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(key=lambda x: x)
print('\n'.join(map(str, arr)))

"""
간단한 정렬 문제
"""