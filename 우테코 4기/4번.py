def solution(s):
    answer = []

    # 맨 처음 반복구간 찾기
    p1, p2 = 0, 0
    while True:
        if s[p1] == s[p2]:
            p2 += 1

        else:
            break

    s += s[p1:p2]
    s = s[p2:]

    # 연속 구간 추출
    p1, p2 = 0, 0
    while p2 < len(s):
        if s[p1] == s[p2]:
            p2 += 1
        else:
            answer.append(p2 - p1)
            p1 = p2
    answer.append(p2 - p1)

    answer.sort()

    return answer