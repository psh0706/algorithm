T = int(input())
nList = [int(input()) for _ in range(T)]


def makeFibonacci(n):
    if n == 1:
        print(1)
        return False

    dp = [1, 1]
    length = 2
    while True:
        temp = dp[length - 1] + dp[length - 2]
        if temp > n:
            break
        else:
            dp.append(temp)
            length += 1

    return dp


def solution():
    for N in nList:
        dp = makeFibonacci(N)

        if not dp:
            continue

        for idx in range(len(dp)-1, -1, -1):
            n = N
            answer = []
            flag = False

            while idx >= 0:
                if n == 0:
                    print(' '.join(map(str, answer)))
                    flag = True
                    break

                if n >= dp[idx]:
                    n -= dp[idx]
                    answer.insert(0, dp[idx])
                else:
                    idx -= 1

            if flag:
                break
    return


solution()


"""
그리디로 푼 9009번
하나의 양의 정수에 대한 피보나치 수들의 합 중 최소개수로 나타낼 수 있는 경우를 찾아내야한다.
최소 개수로 나타낸다는 것은 큰 수부터 greedy 하게 취하면 된다는 것을 의미하기 때문에
피보나치 수열을 테이블을 양의 정수 N보다 작을 때 까지 구해 둔 뒤
큰 수를 취해나가는 방법을 이용했다.
"""
