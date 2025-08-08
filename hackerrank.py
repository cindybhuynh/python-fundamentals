arr = [4, 2, 3, 3, 5, 5, 5]
sorted_arr = sorted(arr, reverse=True)
print(sorted_arr)
i = 0
while (sorted_arr[0] <= sorted_arr[i]):
    i = i + 1
else:
    print(sorted_arr[i])