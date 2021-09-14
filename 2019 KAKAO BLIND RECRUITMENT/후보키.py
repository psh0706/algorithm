from copy import deepcopy
import pandas as pd

relation = [["1", "a", "A", "2"], ["1", "a", "B", "2"], ["2", "b", "B", "3"], ["3", "c", "B", "1"]]
table = pd.DataFrame(relation)
rowLen = len(table)
columnLen = len(table.columns)
superKey = []
print(table)


for i in range(1, columnLen):

    def combination(depth, start, result):
        if depth == i:
            r = list(map(int, result.split()))
            temp = table.iloc[:, r].drop_duplicates()
            print(temp)

            if rowLen == len(temp):
                superKey.append(r)
            return

        for c in range(start, columnLen):
            combination(depth + 1, c + 1, result + str(c) + " ")


    combination(0, 0, "")

candidateKey = deepcopy(superKey)
visit = [False for _ in range(len(superKey))]

for i in range(len(superKey)):
    if visit[i]:
        continue
    A = set(superKey[i])

    for j in range(i+1, len(superKey)):
        if visit[j]:
            continue
        B = set(superKey[j])

        if A.issubset(B):
            candidateKey.remove(superKey[j])
            visit[j] = True

    visit[i] = True

print(candidateKey)


#히든 테케 찾아야함 -> 수정 필요