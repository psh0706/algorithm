def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    linkedList = {i: [i-1, i+1] for i in range(1, n-1)}
    linkedList[0] = [None, 1]
    linkedList[n-1] = [n-2, None]
    pointer = k
    trash = []

    for op in cmd:
        if op == "C":
            [prev, nxt] = linkedList[pointer]
            answer[pointer] = 'X'
            trash.append([pointer, prev, nxt])

            if prev is not None:
                linkedList[prev][1] = nxt

            if nxt is not None:
                linkedList[nxt][0] = prev

            if nxt is None:
                pointer = prev
            else:
                pointer = nxt

        elif op == "Z":
            [p, prev, nxt] = trash.pop(-1)
            answer[p] = 'O'

            if prev is not None:
                linkedList[prev][1] = p

            if nxt is not None:
                linkedList[nxt][0] = p
        else:
            d, num = op.split(" ")
            num = int(num)

            if d == 'U':
                for _ in range(num):
                    pointer = linkedList[pointer][0]
            else:
                for _ in range(num):
                    pointer = linkedList[pointer][1]

    return ''.join(answer)


"""
연결리스트를 직접 구현하는 문제.
"""