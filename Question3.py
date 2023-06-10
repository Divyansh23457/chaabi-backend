def f(list, Key):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j][Key] > list[j + 1][Key]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list




output = f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "fruit")

print(output)
