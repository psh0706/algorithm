n, k = map(int, input().split(" "))
arr = list(map(int, list(input())))
temp = []
p1 = 0
p2 = 0

while p2 < len(arr):
    if not temp:
        temp.append(arr[p2])
        p2 += 1
        continue

    if k == 0:
        temp += arr[p2:]
        break

    if temp[p1] < arr[p2]:
        temp.pop(-1)
        k -= 1
        if p1 == 0:
            continue
        else:
            p1 -= 1
    else:
        temp.append(arr[p2])
        p1 += 1
        p2 += 1


print(''.join(map(str, temp[:len(temp)-k])))


"""
1. 주어진 숫자로 가장 큰 수를 만드는 방법은 내림차순 정렬 하는 것이다.
2. 숫자의 자리를 변경할 수 없으므로, 내림차순에 위배되는 것 들을 지워나간다.
3. 예를 들어 4177252841 같은 숫자의 경우 두번째 1이 지워진 뒤 맨처음 4가 지워지는 순서로 진행되어야 했기 때문에 
   처음에는 위배되는 숫자를 지우고 처음으로 돌아와서 다시 탐색하는 방법을 사용했으나 시간초과로 WC 되었다.
4. 그래서 stack 이용했다. 스택에 값을 하나 하나 넣고, 스택의 top 과 다음 수 사이의 증감 여부를 판단했다.
5. k개 만큼 지워야 했는데 위와 같은 과정을 거치고 나서도 k개가 지워지지 않는 경우가 있었다. (ex. 이미 내림차순 되어있는 경우)
   그럴 경우를 대비해 마지막에 남은 k개 만큼을 떼어주었다.
"""