N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

size = sum(costs)
dp = [0 for _ in range(size+1)]
for i in range(N):
    for j in range(size, -1, -1):
        if j >= costs[i]:
            dp[j] = max(dp[j], dp[j-costs[i]]+memories[i])

ans = 0
for i in range(size+1):
    if dp[i] >= M:
        ans = i
        break

print(ans)

"""
대표적인 DP 알고리즘인 배낭채우기를 응용한 문제이다.
맨처음 greedy 하게 문제를 풀었다가 (cost 오름차순 정렬 후 투포인터 사용) 
반례에 걸려 처음부터 다시 풀었다.. 
-> 1-2-3, 2-4, 1, 2-3-4-5 등등.. 연속적인 조합에 대해서는 연산이 가능하지만
   1-4-5, 1-3-6 등의 조합에 대한 합은 연산이 안되었고 그러한 부분을 그리디하게 표현하기엔 매우 복잡했다.
   냅색 문제가 그리디로 풀리지 않는 이유와 비슷했다. 최적화된 연산이 필요했음.
   
knapsack 문제에서는 용량을 기준으로 두고 각 용량에서 cost 가 최대가 되는 최적화를 찾아나간다.
하지만 이 문제는 반대로 dp 점화식을 세워야 가능.
cost를 기준으로 각 cost 에서 memory가 최대가 되는 최적화를 찾아 나간다.

참고로 8번 line 에서 역순으로 순회하는 이유는
오름차순으로 순회할 경우
ex) cost를 1이라고 할 때 (i=1)
dp[2] 에서 dp[1]을 가져오며 m[i]을 한번 더하고
dp[3] 에서 dp[2]를 가져오며 m[i]를 한번 더하며 m[i]를 누적하기 때문임.
"""