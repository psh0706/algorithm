def solution(s):
    answer = 0
    numList = []
    strList = list(s)
    word = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    temp = ""
    for string in strList:
        if string.isdigit():
            numList.append(string)
        else:
            temp += string
            if temp in word:
                numList.append(word[temp])
                temp = ""

    answer = int(''.join(numList))

    return answer


"""
hash map (= dictionary) 에 미리 저장해둔 단어를 매칭
"""