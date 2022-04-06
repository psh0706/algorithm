def solution():
    n = int(input())
    alphabet = {}
    words = []
    string = ''

    # 정보 저장 -> words : 단어 정보, alphabet : 등장 하는 알파벳의 정보
    for i in range(n):
        word = input()
        string += word
        words.append(word)
    alphabet = dict.fromkeys(set(list(string)), 0)

    # 알파벳이 등장하는 각 자리수를 기준으로 가중치 계산 후, 가중치 정렬
    # 1의 자리수, 10의 자리수 , 100의 자리수 ...
    for word in words:
        for i in range(len(word)):
            alphabet[word[i]] += 10 ** (len(word) - i - 1)
    values = list(alphabet.items())
    values.sort(key=lambda x: -x[1])

    # 가중치가 높은 것 부터 숫자 부여
    cnt = 9
    for value in values:
        alphabet[value[0]] = cnt
        cnt -= 1

    # 숫자로 치환 후 계산
    answer = 0
    for word in words:
        string = ''
        for i in range(len(word)):
            string += str(alphabet[word[i]])
        answer += int(string)

    return answer


print(solution())


"""
알파벳이 많이 등장할 수록, 높은 자리수에 등장 할 수록 높은 수를 부여해야 
덧셈에서 가장 큰 수를 찾을 수 있다.
그래서 알파벳 별로 알파벳이 등장하는 횟수와 자리수를 모두 고려헤 가중치를 두었다.
예를들어 한 단어가 등장하고 그것이 AAA 인 경우 
A의 가중치는 100 + 10 + 1 이다.
두 단어가 등장하고 그것이 ABC, AA 인 경우 
A의 가중치는 100 + 10 + 1 이며, B의 가중치는 10, C의 가중치는 1이다.
가중치를 구한 뒤 정렬해서 우선순위가 높은 순서대로 큰 숫자를 부여했다.
알파벳과 숫자를 맵핑 시켜주고 덧셈하면 끝
"""