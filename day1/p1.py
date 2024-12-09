with open("input.txt", "r") as file:
    left = []
    right = []
    res = []
    for line in file:
        arr = line.split("   ")
        left.append(arr[0].strip())
        right.append(arr[1].strip())
    while len(left) > 0:
        res.append(
            abs(
                int(left.pop(left.index(min(left))))
                - int(right.pop(right.index(min(right))))
            )
        )
    print(sum(res))
