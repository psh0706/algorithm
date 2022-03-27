N = int(input())
length = int(input())
S = input()
pLen = 2 * N + 1
idx = 0
answer = 0

while True:
    if length - idx < pLen:
        break

    if S[idx] != "I":
        idx += 1
        continue

    count = 0
    for i in range(N):
        if S[idx + (i*2)] == "I" and S[idx + (i*2) + 1] == "O":
            count += 1
            continue
        else:
            break

    if count == N and S[idx + (count * 2)] == "I":
        count2 = 0
        idx2 = idx + count * 2
        i = 0
        while idx2 + (i*2) < length - 2:
            # print(S[idx2 + (i * 2)], S[idx2 + (i * 2) + 1])
            if S[idx2 + (i * 2)] == "I" and S[idx2 + (i * 2) + 1] == "O":
                count2 += 1
                i += 1
                continue
            else:
                if S[idx2 + (i * 2)] != "I":
                    count2 -= 1
                break

        answer += 1 + count2
        idx += (N + count2)*2 + 1
    else:
        idx += count * 2 + 1

print(answer)
