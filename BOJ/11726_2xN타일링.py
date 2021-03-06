n = int(input())

cnt = [0 for _ in range(n+1)]

cnt[0], cnt[1] = 1, 1

for i in range(2, n+1):
    cnt[i] = (cnt[i-2] + cnt[i-1])%10007

print(cnt[-1])

"""
엄청나게 대표적인 DP 문제인 피보나치 수열
처음에는 모양에서 최적화를 찾으려 했는데
정답은 개수에 있었다...
그리고 출력값을 10007로 나누라는 조건이 있었는데
왜 있는건가 했더니 피보나치의 수가 나중에는 걷잡을수 없이 커져서 였다.
파이썬은 자동으로 큰 정수를 지원해주지만 다른언어들은 아니니..
(n+m)%k = n%k + m%k 인 점을 이용해서 피보나치를 계산할 때마다 나머지 연산을 했다 (큰 수 방지!).
"""