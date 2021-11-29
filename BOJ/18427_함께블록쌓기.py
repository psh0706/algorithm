N, M, H = map(int, input().split())
students = []
cnt = 0

for _ in range(N):
    line = list(map(int, input().split()))
    students.append(line)
#
#
# def recursion(depth, result):
#     if result == H:
#         global cnt
#         cnt += 1
#         return
#
#     if depth == N:
#         return
#
#     for value in students[depth]:
#         if result + value > H:
#             return
#         recursion(depth+1, result+value)
#
#
# recursion(0, 0)
# print(cnt % 10007)

dp = [[0 for _ in range(H+1)] for _ in range(N)]
for i in range(N):
    if i == 0:
        dp[i][0] = 1
        for s in students[i]:
            dp[i][s] = 1
        continue
    for j in range(H+1):
        if j == 0:
            dp[i][j] = 1
            continue

        # i번 학생이 높이 j를 만들 수 있는 모든 블럭에 대해 경우의 수 더하기
        accCase = 0
        for s in students[i]:
            # 높이 - 가진 블럭 높이가 0보다 작으면 안된다.
            if j - s >= 0:
                accCase += dp[i-1][j-s]

        # dp[i-1][j] 은 i번 학생이 j높이를 만들기 위해 블럭을 놓지 않은 경우
        dp[i][j] += dp[i-1][j] + accCase

print(dp[N-1][H])

"""
재귀로 잘못 접근해서 많이 돌아간 문제 ㅠㅠ
배낭채우기를 응용한 dp 문제였다.

* 주의사항
- 한 사람당 한개의 블럭만 놓을 수 있다.
- 높이에 꼭 맞게 놓은 경우의 수를 체크한다.

i를 학생의 수만큼 순회하며 블럭을 하나 하나 쌓는다고 가정하자.
그리고 높이 j를 0 부터 목표 높이 H까지 하나하나 따져준다.

dp[i][j] = k 는
i번째 학생이 j 높이의 블럭을 쌓을 때 k라는 경우의 수를 가진다는 의미이다.

위 식은 아래와 같이 나타낼 수 있다.
dp[i][j] = dp[i - 1][j] + dp[i - 1][j - students[i][s]]

첫 번째 항인 dp[i - 1][j]는 i-1번째 학생이 j 높이를 쌓았을 때의 경우의 수이다. (최적화 된 값)
이는 i번째 학생이 j라는 높이를 만들기 위해 블럭을 놓지 않은 경우를 뜻한다.

두 번째 항인 dp[i - 1][j - students[i][s]]는 i-1번째 학생이 j - students[i][s] 높이를 쌓았을 때의 경우의 수이다.
students[i][s] 는 i번째 학생이 가진 블럭의 높이들이다. 예를 들어 아래와 같다.
students[2] = [1, 2, 3] // 2번학생이 가진 블럭은 1, 2, 3이 있다.
이것이 의미하는것은 아래와 같다. 높이인 j 가 4일때 라고 하겠다.
2번째 학생이 높이가 1인 블럭을 놓기 전에 1번째 학생이 4 - 1 = 3 만큼 놓아두었던 블럭에 본인이 가진 블럭을 얹기만 하면 된다.
2번째 학생이 높이가 2인 블럭을 놓기 전에 1번째 학생이 4 - 2 = 2 만큼 놓아두었던 블럭에 본인이 가진 블럭을 얹기만 하면 된다.
2번째 학생이 높이가 1인 블럭을 놓기 전에 1번째 학생이 4 - 3 = 1 만큼 놓아두었던 블럭에 본인이 가진 블럭을 얹기만 하면 된다.
(위의 주의사항 덕에 가능한 조건들이다.)
주의해야 할 것은 높이가 4일때를 구하려 하는데 4보다 큰 블럭을 놓을수는 없다는 점이다. (j - s >= 0)

첫 번째 항과 두 번째 항을 모두 구해 더해주면 i번째 학생이 j 높이에 블럭을 놓을 수 있는 경우의 수를 구할 수 있다.
"""