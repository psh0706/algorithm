n = int(input())
words = [input() for _ in range(n)]
words = list(set(words))
words.sort(key=lambda x: (len(x), x.lower()))
for word in words:
    print(word)

"""
정렬 문제
조건이 2개일때 순차적으로 정렬할수있어야한다.
"""