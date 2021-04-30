"""
Given an unsorted array of integers, find a continuous subarray which adds to a given number.
Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4
Sum of elements between indices
2 and 4 is 20 + 3 + 10 = 33
Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4
Sum of elements between indices
1 and 4 is 4 + 0 + 0 + 3 = 7
Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
There is no subarray with 0 sum
"""


def find_continuous_subarray(input_arr, total_sum):
    start = 0
    end = 1
    n = len(input_arr)
    max_sum = input_arr[0]
    while end <= n:
        while max_sum > total_sum and start < end - 1:
            max_sum -= input_arr[start]
            start = start + 1
            print(max_sum, '---', start, '---', end)
        if max_sum == total_sum:
            print('subarray found between ', start, ' and ', end - 1)
            return start, end
        if end < n:
            max_sum += input_arr[end]
            print(max_sum)
        end = end + 1
    print('No subarray found')
    return


arr1 = [1, 4, 20, 3, 10, 5]
sum1 = 33
arr2 = [1, 4, 0, 0, 3, 10, 5]
sum2 = 7
arr3 = [1, 4]
sum3 = 0
arr4 = [0, -3, -2, 7, -2, 5]
sum4 = -5
find_continuous_subarray(arr1, sum1)
find_continuous_subarray(arr2, sum2)
find_continuous_subarray(arr3, sum3)
find_continuous_subarray(arr4, sum4)
