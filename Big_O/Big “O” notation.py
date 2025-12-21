# 1) Check if string is a palindrome
def is_palindrome(s):
    return s == s[::-1]


# 2) Find two numbers in sorted array that sum to target
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return (arr[left], arr[right])
        elif total < target:
            left += 1
        else:
            right -= 1
    return -1


# 3) Max profit from stock prices (single buy/sell)
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)

    return max_profit


# 4) Move all zeros to end without extra list--
def move_zeros(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1


# 5) Find the single number using XOR
def single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result


# 6) Find three numbers summing to target in a sorted list
def three_sum_sorted(arr, target):
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == target:
                return (arr[i], arr[left], arr[right])
            elif total < target:
                left += 1
            else:
                right -= 1
    return -1


# 7) Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# -----------------------
# EXAMPLE USAGE:
# -----------------------

print("Palindrome:", is_palindrome("level"))
print("Two Sum:", two_sum_sorted([1, 2, 3, 4, 6], 7))
print("Max Profit:", max_profit([7, 1, 5, 3, 6, 4]))

arr1 = [0, 1, 0, 3, 12]
move_zeros(arr1)
print("Move Zeros:", arr1)

print("Single Number:", single_number([2, 2, 1]))
print("Three Sum:", three_sum_sorted([1, 2, 4, 5, 6, 8], 13))

arr2 = [5, 1, 4, 2, 8]
bubble_sort(arr2)
print("Bubble Sort:", arr2)