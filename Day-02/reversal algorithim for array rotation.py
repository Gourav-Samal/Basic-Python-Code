def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
arr = [10, 20, 30, 40, 50]
k = 2
n = len(arr)
reverse(arr, 0, k-1)
reverse(arr, k, n-1)
reverse(arr, 0, n-1)
print(arr)

