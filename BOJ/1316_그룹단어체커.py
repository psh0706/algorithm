n = int(input())
words = [input() for _ in range(n)]

for word in words:
    visit = [False for _ in range(26)]
    word += " "

    for i in range(len(word)-1):
        if visit[ord(word[i]) - 97]:
            n -= 1
            break

        if word[i] != word[i+1]:
            visit[ord(word[i]) - 97] = True

print(n)
"""
그룹 단어인 단어의 갯수를 출력하는 문제.
방문처리를 이용하여 풀었다.
"""