def min_operations(arr, k):
    n = len(arr)

    for i in range(1, n):
        if (arr[i] - arr[0]) % k != 0:
            return -1


    arr.sort()
    median = arr[n // 2]

    operations = 0
    for num in arr:
        operations += abs(num - median) // k

    return operations


data = list(map(int, input().split()))

n = data[0]
arr = data[1:n+1]
k = data[n+1]

print(min_operations(arr, k))