def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
short_list = [5, 2, 9, 1, 5]
long_list = [3, 6, 8, 2, 7, 4, 1, 9, 5]
sorted_short = bubble_sort(short_list)
sorted_long = bubble_sort(long_list)
print("Sorted Short List:", sorted_short)
print("Sorted Long List:", sorted_long)