with open("input.txt", "r") as file:
    left = []
    right = []
    res = []
    for line in file:
        arr = line.split("   ")
        left.append(arr[0].strip())
        right.append(arr[1].strip())
    for num in left:
        res.append(int(num) * int(right.count(num)))
    print(sum(res))
