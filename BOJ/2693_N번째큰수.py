for _ in range(int(input())):
    li = sorted(map(int, input().split()))
    print(li[-3])

"""
이틀동안 바빠서 한 문제도 못푼게 아쉬워 풀어본 문제
항상 3번째 큰 수를 출력해야 하므로 받은 문자열을 정수리스트로 만들어 정렬해주었다.
리스트가 아니기 때문에 리스트 메서드인 sort 가 아니라 
내장함수 sorted 를 사용했다.
"""