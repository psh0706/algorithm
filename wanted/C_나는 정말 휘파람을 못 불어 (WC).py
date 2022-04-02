n = int(input())
S = list(input())
E_CNT = 0
temp_E_CNT = 0
answer = 0
MOD = 1000000007
value = 0
H_TEMP = 0

for i in range(n-1, -1, -1):
    if S[i] == 'E':
        if E_CNT == 0:
            E_CNT = 1
        elif E_CNT == 1:
            E_CNT = 2
            value = 1
        else:
            value = (value*2 + E_CNT) % MOD
            E_CNT += 1
        continue

    if S[i] == 'H':
        H_TEMP = (H_TEMP + value) % MOD
        continue

    if S[i] == 'W':
        answer += H_TEMP


print(answer)
