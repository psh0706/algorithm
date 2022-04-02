def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        applicant = []
        for i in range(n):
            applicant.append(list(map(int, input().split())))
        applicant.sort(key=lambda x: x[0])

        drop = 0
        bMax = 0
        for i in range(n):
            if i == 0:
                bMax = applicant[i][1]
                continue

            if bMax < applicant[i][1]:
                drop += 1
            else:
                bMax = applicant[i][1]

        print(n - drop)


solution()

"""
1. 서류 점수로 정렬
2. 정렬 된 지원자 순서대로 면접 점수 확인
3. 이미 서류 점수로 정렬 되어있기 때문에 뒤에있는 지원자는 이미 앞의 지원자들에게 한 번 떨어진 것이다.
   따라서 앞의 지원자를 면접 점수로 모두 제쳐야만 선발될 수 있다.
   -> 면접 점수가 앞의 지원자들보다 높을 때만 선발된다. 높지 않으면 탈락 (drop += 1)
4. drop 된 사람들을 제외한 사람들이 선발 된다. (n - drop) 
"""

