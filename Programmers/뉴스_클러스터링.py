def solution(str1, str2):
    answer = 0
    jacad = 0
    str1 = str1.lower()
    str2 = str2.lower()

    set1 = []
    set2 = []

    for i in range(len(str1) - 1):
        if str1[i].islower() and str1[i + 1].islower():
            set1.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        if str2[i].islower() and str2[i + 1].islower():
            set2.append(str2[i] + str2[i + 1])

    interSet = set(set1) & set(set2)
    unionSet = set(set1) | set(set2)

    interMultiple = sum([min(set1.count(i), set2.count(i)) for i in interSet])
    unionMultiple = sum([max(set1.count(i), set2.count(i)) for i in unionSet])

    if unionMultiple == 0:
        jacad = 1
    else:
        jacad = interMultiple / unionMultiple

    answer = int(jacad * 65536)
    print(answer)

    return answer


a = input()
b = input()
solution(a, b)


"""
1. 모든 문자열 소문자화
2. 다중 집합 원소 생성 -> 이때 특문, 공백, 숫자 들어간 원소는 포함하지 않음
3. 다중집합을 일반집합으로 표현하여 교집합, 합집합 구하기 (interSet, unionSet)
4. 일반 집합의 교집합 원소 i 가 다중집합에 몇 개 있는지 두 집합 모두 확인 => 그 중 적은것이 다중 교집합의 원소
   모두 더하기 => 다중집합 간의 교집합의 수
5. 일반 집합의 힙집합 원소 i 가 다중집합에 몇 개 있는지 두 집합 모두 확인 => 그 중 큰것이 다중 합집합의 원소
   모두 더하기 => 다중집합 간의 합집합의 수
6. 자카드 = 다중집합 교집합 수 / 다중집합 합집합 수
7. 합집합이 공집합 => 무조건 두 집합 다 공집합 이라는 이야기 이므로 jacad 1로 설정
8. 계산
"""