def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


nums = [1 , 88, 8,4 ,84, 84,5, 4,64 ,46 ]
sorted_nums = selection_sort(nums)
print(sorted_nums)
