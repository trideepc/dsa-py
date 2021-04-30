

def binary_search(arr, start, end, x):
    if end >= start:
        mid = start + (end - start)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, end, x)
        else:
            return binary_search(arr, start, mid - 1, x)
    return -9999


array = [2, 3, 4, 10, 15, 40, 15, 15]
num = 15

result = binary_search(array, 0, len(array) - 1, num)

if result != -9999:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
