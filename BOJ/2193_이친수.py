N = int(input())
arr = [0 for _ in range(N+1)]
arr[1] = 1

for i in range(2, N+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[-1])

"""
결국은 피보나치였던 dp 문제.
"""