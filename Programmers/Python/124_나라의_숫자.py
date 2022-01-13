def solution(n):
    answer = ''

    while n > 0:
        if n % 3:
            answer = str(n % 3) + answer
            n = int(n / 3)
        else:
            answer = '4' + answer
            n = int(n / 3) - 1

    print(answer)
    return answer


N = int(input())
solution(N)

"""
3진수를 구하는 것 처럼 계속 3으로 나누어주는데,
기존 3진수에서는 1, 2, 0 으로 숫자를 구성하기 때문에
예를들어 3을 3진수로 나타낼 때 0이 아니라 10 으로 나타내었다.
본 문제에서는 1, 2, 4로 숫자를 구성하기 때문에
3을 나타낼 때 4로 나타내게 된다. (3진수와의 차이점)

따라서 수를 3으로 나누었을 때 나머지가 0이라면 (3의 배수이면)
n / 3 의 몫에서 1을 추가적으로 빼 주어야 한다. 
"""
