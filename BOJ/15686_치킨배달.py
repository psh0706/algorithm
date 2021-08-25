N, M = map(int, input().split())
c_list = list()
h_list = list()

# 치킨집과 집의 위치 정리
for i in range(N):
    li = input().split()
    for j in range(N):
        if li[j] == '2':
            c_list.append([i, j])
        elif li[j] == '1':
            h_list.append([i, j])


# M에 맞추어 치킨집 유무 리스트 작성
def mList(depth, start, isC_list):
    if depth == M:
        m_list.append([x for x in isC_list])
        return

    for c in range(start, len(c_list)):
        isC_list.append(c_list[c])
        mList(depth+1, c+1, isC_list)
        isC_list.pop()


m_list = list()
mList(0, 0, [])

# 각 경우 별 도시치킨거리 구하기
c_len = []
for cases in m_list:
    acc = 0
    for home in h_list:
        mini = 100
        for case in cases:
            length = abs(case[0]-home[0]) + abs(case[1]-home[1])
            if length < mini:
                mini = length
        acc += mini
    c_len.append(acc)

print(min(c_len))

