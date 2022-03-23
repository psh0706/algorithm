def calc(a, op, b):
    if op == "*":
        return a * b
    elif op == "+":
        return a + b
    elif op == "-":
        return a - b


def solution():
    n = int(input())
    arr = list(input())

    if n == 1:
        print(arr[0])
        return

    dp = [[] for _ in range(int(n / 2) + 1)]
    for i in range(n):
        if i % 2 == 0:
            arr[i] = int(arr[i])

    dp[0] = [arr[0]]

    for idx in range(1, int(n / 2) + 1):
        i = idx * 2 - 1

        if i == 1:
            dp[idx] = [calc(arr[i - 1], arr[i], arr[i + 1])]
            continue
        else:
            for prev in dp[idx - 1]:
                dp[idx].append(calc(prev, arr[i], arr[i + 1]))

            bracket = calc(arr[i - 1], arr[i], arr[i + 1])
            for prev in dp[idx - 2]:
                dp[idx].append((calc(prev, arr[i - 2], bracket)))

            dp[idx] = list(set(dp[idx]))

    print(max(dp[-1]))


solution()

"""
처음에는 1차원 DP로 풀어서 틀렸다. 
-> $은 연산자라는 의미이다.
-> max(dp[idx-2] $arr[i-2] (arr[i-1] $arr[i] arr[i+1]), dp[idx-1] $arr[i] arr[i+1])

하지만 무조건 앞에서부터 높은 값만을 취하면 안되고, 앞에서 음수가 나오더라도 뒤에서 큰값이 될 수 있으므로
모든 괄호 조건을 탐색해야한다.
-> 위 식의 반례
-> 19
   2*1-1*1+2*2-9*8-9*9

시간 제한이 0.5초 이지만 N이 (수식의 길이가) 19로 매우 작으므로 완탐이 가능하다.
조합식 등으로도 풀 수 있을 것 같지만, 메모제이션을 이용해서 풀어보았다. (결국 모든 경우의 수를 푸는것은 같다.)
"""