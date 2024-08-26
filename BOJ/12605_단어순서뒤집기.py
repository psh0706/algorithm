def solution():
    n = int(input())
    texts = []

    for _ in range(n):
        texts.append(input())

    for i in range(n):
        a = texts[i].split(" ");
        b = list(reversed(a));
        print("Case #"+str(i+1)+": "+" ".join(b));


solution();

# 복귀 기념 짧은 문제 풀어보기