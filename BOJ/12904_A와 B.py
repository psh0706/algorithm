S = list(input())
T = list(input())
r = False

for _ in range(len(T) - len(S)):
    if not r:
        char = T.pop(-1)
    else:
        char = T.pop(0)

    if char == "A":
        continue
    else:
        r = not r

if r:
    T.reverse()

if S == T:
    print(1)
else:
    print(0)

"""
S를 T로 만드는것이 아니라
T를 한자 한자 지우며 S로 만들어야한다.
"""