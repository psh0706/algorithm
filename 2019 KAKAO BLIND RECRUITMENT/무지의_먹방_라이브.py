k = 6
food_times = [1, 1, 2, 2]
length = len(food_times)
visit = [False for _ in range(len(food_times))]
pointer = 0


while sum(food_times) != 0:
    if visit[pointer]:
        pointer = 0 if (pointer + 1) == length else pointer + 1
        continue

    if k == 0:
        break

    food_times[pointer] -= 1
    if food_times[pointer] == 0:
        visit[pointer] = True

    pointer = 0 if (pointer + 1) == length else pointer+1
    k -= 1


if sum(food_times) == 0:
    print(-1)
else:
    print(pointer+1)
