def solution():
    n = int(input())
    houses = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(3)] for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + houses[i - 1][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + houses[i - 1][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + houses[i - 1][2]

    print(min(dp[-1]))
    return


solution()

"""
<RGB 거리>
→ 단순하게 매번 최소값을 선택해 나가기? 안됨. (예제 5번이 예시)
→ 지금거 + 다음거를 더했을때 가장 최소가 되는 지금거를 선택 
이 방법은 바로 다음것 까지의 최소를 미리 체크함.
왜냐면 어차피 색상의 영향을 미치는건 바로 다음 집밖에 없음.
그래서 그냥 바로 다음집 까지만 최소체크 해주면 됨.

→ 틀렸습니다 1회 : 제일 마지막집 앞집이랑 색 겹치면 안되는데 그냥 모든 색에 대해서 min 해버림
→ 틀렸습니다 2회 :  mini 초기값 2000 에서 2001로 변경. (찐으로 2000이 나올 경우 비교문 들어가지 않아서
idx 값 바뀌지 않음.) 근데 이게 문제가 아니였는지 다시 틀림.
→ 틀렸습니다 3회 : 

반례 ) 3
      1 2 3
      1 2 3
      100 1 100

      답 : 4

      오답 : 5

같은 mini 값이 나올 때의 문제였음 
내가 생각한 로직으로는
1→ 3 → 1 이 나오는데
답은 2→ 1 → 1 로 4임.
이것은 가장 처음 1+2, 2+1를 비교하면서 달라지는것.
결론 : 그리디가 아니라 DP

DP로 풀어서 성공
"""